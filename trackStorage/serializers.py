# serializers.py
from rest_framework import serializers
from .models import Trip, Point

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        exclude = ('id', 'trip')  # We'll handle trip relationship separately

class TripSerializer(serializers.ModelSerializer):
    trip = PointSerializer(many=True)  # Nested serializer for points
    
    class Meta:
        model = Trip
        fields = '__all__'
    
    def create(self, validated_data):
        points_data = validated_data.pop('trip')
        trip = Trip.objects.create(**validated_data)
        
        # Create all points for this trip
        points = [
            Point(trip=trip, **point_data)
            for point_data in points_data
        ]
        Point.objects.bulk_create(points)
        
        return trip