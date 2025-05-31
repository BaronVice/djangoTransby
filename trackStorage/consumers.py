from channels.generic.websocket import AsyncWebsocketConsumer
from django.apps import apps
import json
import logging
from asgiref.sync import sync_to_async
from .datastructures import *
from .utils import split_activities, set_v_or_else_mean, existingActivitiesLen, to_ignore
import asyncio

logger = logging.getLogger(__name__)

class TransportConsumer(AsyncWebsocketConsumer):
    @property
    def model_pool(self) -> ObjectPool:
        """Thread-safe access to the global model pool"""
        return apps.get_app_config('trackStorage').model_pool
    
    @property
    def mean_values(self) -> dict:
        """Thread-safe access to the global model pool"""
        return apps.get_app_config('trackStorage').mean_values
    
    @property
    def mean_values_len(self) -> int:
        """Thread-safe access to the global model pool"""
        return apps.get_app_config('trackStorage').mean_values_len

    async def connect(self):
        """Connection already authenticated by ASGI middleware"""
        self.trip_uid = self.scope['url_route']['kwargs']['trip_uid']
        
        # Add to trip-specific group
        await self.channel_layer.group_add(
            f"trip_{self.trip_uid}",
            self.channel_name
        )
        
        await self.accept()
        logger.info(f"New WebSocket connection for trip {self.trip_uid}")


    async def disconnect(self, close_code):
        """Clean up on disconnect"""
        await self.channel_layer.group_discard(
            f"trip_{self.trip_uid}",
            self.channel_name
        )
        logger.info(f"Disconnected from trip {self.trip_uid}")


    async def receive(self, text_data):
        """Handle incoming sensor data"""
        try:
            data = json.loads(text_data)
            data = data['request']

            # Validate required fields
            if 'accelerometerMin' not in data:
                await self.send_error("No sensors in data. Any chance you use old version?")
                return
            
            sensor_data = split_activities(data['registeredActivities'])
            sensor_data_len = 0
            k_lower = ""
            for k,v in data.items():
                k_lower = k.lower()

                if k_lower in to_ignore: continue

                if k_lower not in self.mean_values:
                    logger.warning(f"{k.lower()} is not expected, skipped")
                    continue
                
                sensor_data[k_lower] = set_v_or_else_mean(v, self.mean_values[k_lower])
                sensor_data_len += 1
            
            if sensor_data_len != self.mean_values_len:
                raise Exception(f'sensor_data_len: {sensor_data_len - existingActivitiesLen} != {self.mean_values_len}')

            # Process prediction (reuse your existing logic)
            prediction = await self.predict_transport(sensor_data)
            
            # Send response
            await self.send(json.dumps({
                "type": "transport_prediction",
                "point_id": data['point_id'],
                "probabilities": prediction,
            }, ensure_ascii=False))

            
        except json.JSONDecodeError:
            await self.send_error("Invalid JSON format")
        except Exception as e:
            logger.error(f"Processing error: {str(e)}")
            await self.send_error("Processing failed")


    async def send_error(self, message):
        """Standardized error response"""
        await self.send(json.dumps({
            "type": "error",
            "message": message
        }))


    async def predict_transport(self, sensor_data):
        """Acquire model, predict, and release safely"""
        model: ReusableClassifier = None
        try:
            # Non-blocking acquire with timeout
            start_time = asyncio.get_event_loop().time()
            while (asyncio.get_event_loop().time() - start_time) < 10:  # 10s timeout
                model = await sync_to_async(self.model_pool.acquire, thread_sensitive=False)()
                if model:
                    logger.info(f"Classifier acquired {model.id}")
                    prediction = await sync_to_async(model.predict, thread_sensitive=False)(sensor_data)
                    return prediction
                await asyncio.sleep(0.3)
            
            logger.error(f"No model available in pool")
            raise TimeoutError("Model pool exhausted")
        
        finally:
            if model:
                await sync_to_async(self.model_pool.release, thread_sensitive=False)(model)
                logger.info(f"Classifier released {model.id}")
