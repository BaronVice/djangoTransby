from django.db import models

# Create your models here.

class Trip(models.Model):
    trip_uid = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, blank=True, null=True)
    socialstatus = models.CharField(max_length=100, blank=True, null=True)
    financialsituation = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    startplacetype = models.CharField(max_length=100)
    endplacetype = models.CharField(max_length=100)
    cost = models.IntegerField()
    transportationcosts = models.CharField(max_length=100, blank=True, null=True)
    general_comment = models.CharField(max_length=100, blank=True, null=True)
    trip_comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Trip {self.trip_uid}"


class Point(models.Model):
    trip = models.ForeignKey(
        'Trip',
        on_delete=models.CASCADE,
        related_name='points'
    )

    # Location data
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    timestamp = models.DateTimeField()
    
    # Movement metrics
    speed = models.FloatField()
    speedAccuracy = models.FloatField()
    distance = models.FloatField()
    locationAccuracy = models.FloatField()
    ptstop = models.BooleanField(default=False)
    
    # Sensor data - Rotation
    rotationMagnitudeStd = models.FloatField()
    rotationMagnitudeMean = models.FloatField()
    rotationMagnitudeMin = models.FloatField()
    rotationMagnitudeMax = models.FloatField()
    rotationAngleStd = models.FloatField()
    rotationAngleMean = models.FloatField()
    rotationAngleMin = models.FloatField()
    rotationAngleMax = models.FloatField()
    
    # Sensor data - Gyroscope
    gyroscopeMagnitudeStd = models.FloatField()
    gyroscopeMagnitudeMean = models.FloatField()
    gyroscopeMagnitudeMin = models.FloatField()
    gyroscopeMagnitudeMax = models.FloatField()
    gyroscopeTurnRateStd = models.FloatField()
    gyroscopeTurnRateMean = models.FloatField()
    gyroscopeTurnRateMin = models.FloatField()
    gyroscopeTurnRateMax = models.FloatField()
    gyroscopeUncalibratedMagnitudeStd = models.FloatField()
    gyroscopeUncalibratedMagnitudeMean = models.FloatField()
    gyroscopeUncalibratedMagnitudeMin = models.FloatField()
    gyroscopeUncalibratedMagnitudeMax = models.FloatField()
    
    # Sensor data - Game Rotation
    gameRotationAngleStd = models.FloatField()
    gameRotationAngleMean = models.FloatField()
    gameRotationAngleMin = models.FloatField()
    gameRotationAngleMax = models.FloatField()
    gameRotationMagnitudeStd = models.FloatField()
    gameRotationMagnitudeMean = models.FloatField()
    gameRotationMagnitudeMin = models.FloatField()
    gameRotationMagnitudeMax = models.FloatField()
    
    # Sensor data - Accelerometer
    accelerometerMean = models.FloatField()
    accelerometerMin = models.FloatField()
    accelerometerMax = models.FloatField()
    accelerometerStd = models.FloatField()
    linearAccelerationMean = models.FloatField()
    linearAccelerationMin = models.FloatField()
    linearAccelerationMax = models.FloatField()
    linearAccelerationStd = models.FloatField()
    
    # Sensor data - Gravity
    gravityMagnitudeMean = models.FloatField()
    gravityMagnitudeMin = models.FloatField()
    gravityMagnitudeMax = models.FloatField()
    gravityMagnitudeStd = models.FloatField()
    gravityPitchMean = models.FloatField()
    gravityPitchMin = models.FloatField()
    gravityPitchMax = models.FloatField()
    gravityPitchStd = models.FloatField()
    gravityRollMean = models.FloatField()
    gravityRollMin = models.FloatField()
    gravityRollMax = models.FloatField()
    gravityRollStd = models.FloatField()
    
    # Sensor data - Magnetometer
    magneticFieldStrengthMean = models.FloatField()
    magneticFieldStrengthMin = models.FloatField()
    magneticFieldStrengthMax = models.FloatField()
    magneticFieldStrengthStd = models.FloatField()
    magneticFieldUncalibratedHardIronMean = models.FloatField()
    magneticFieldUncalibratedHardIronMin = models.FloatField()
    magneticFieldUncalibratedHardIronMax = models.FloatField()
    magneticFieldUncalibratedHardIronStd = models.FloatField()
    magneticFieldUncalibratedSoftIronMean = models.FloatField()
    magneticFieldUncalibratedSoftIronMin = models.FloatField()
    magneticFieldUncalibratedSoftIronMax = models.FloatField()
    magneticFieldUncalibratedSoftIronStd = models.FloatField()
    
    # Sensor data - Pressure
    pressureMean = models.FloatField()
    pressureMin = models.FloatField()
    pressureMax = models.FloatField()
    pressureStd = models.FloatField()
    
    # Activity data
    stepCounterMean = models.FloatField()
    stepCounterMin = models.FloatField()
    stepCounterMax = models.FloatField()
    stepCounterStd = models.FloatField()

    transportTypeUsedToNextPoint = models.CharField(max_length=100)
    registeredActivities = models.CharField(max_length=100)

    def __str__(self):
        return f"Point at ({self.latitude}, {self.longitude}) - {self.timestamp}"