from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TripSerializer
import logging
import json

logger = logging.getLogger(__name__)

class TripCreateView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # If receiving raw JSON data
            if isinstance(request.data, str):
                data = json.loads(request.data)
            else:
                data = request.data
            
            serializer = TripSerializer(data=data)
            if serializer.is_valid():
                trip = serializer.save()
                logger.info(f"Saved (trip_uid {trip.trip_uid})")

                return Response({
                    'status': 'success',
                    'trip_uid': trip.trip_uid,
                    'points_count': trip.points.count()
                }, status=status.HTTP_201_CREATED)
            
            return Response({
                'status': 'error',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            logger.error(f"500: {str(e)}")
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)