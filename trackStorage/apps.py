from django.apps import AppConfig


class TrackstorageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trackStorage'
    model_pool = None

    def ready(self):
        # Initialize pool when app starts
        from trackStorage.datastructures import ObjectPool
        
        self.model_pool = ObjectPool(size=5)
