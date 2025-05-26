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
    speedaccuracy = models.FloatField()
    distance = models.FloatField()
    locationaccuracy = models.FloatField()
    ptstop = models.BooleanField(default=False)
    
    # Sensor data - rotation
    rotationmagnitudestd = models.FloatField()
    rotationmagnitudemean = models.FloatField()
    rotationmagnitudemin = models.FloatField()
    rotationmagnitudemax = models.FloatField()
    rotationanglestd = models.FloatField()
    rotationanglemean = models.FloatField()
    rotationanglemin = models.FloatField()
    rotationanglemax = models.FloatField()
    
    # Sensor data - Gyroscope
    gyroscopemagnitudestd = models.FloatField()
    gyroscopemagnitudemean = models.FloatField()
    gyroscopemagnitudemin = models.FloatField()
    gyroscopemagnitudemax = models.FloatField()
    gyroscopeturnratestd = models.FloatField()
    gyroscopeturnratemean = models.FloatField()
    gyroscopeturnratemin = models.FloatField()
    gyroscopeturnratemax = models.FloatField()
    gyroscopeuncalibratedmagnitudestd = models.FloatField()
    gyroscopeuncalibratedmagnitudemean = models.FloatField()
    gyroscopeuncalibratedmagnitudemin = models.FloatField()
    gyroscopeuncalibratedmagnitudemax = models.FloatField()
    
    # Sensor data - Game rotation
    gamerotationanglestd = models.FloatField()
    gamerotationanglemean = models.FloatField()
    gamerotationanglemin = models.FloatField()
    gamerotationanglemax = models.FloatField()
    gamerotationmagnitudestd = models.FloatField()
    gamerotationmagnitudemean = models.FloatField()
    gamerotationmagnitudemin = models.FloatField()
    gamerotationmagnitudemax = models.FloatField()
    
    # Sensor data - Accelerometer
    accelerometermean = models.FloatField()
    accelerometermin = models.FloatField()
    accelerometermax = models.FloatField()
    accelerometerstd = models.FloatField()
    linearaccelerationmean = models.FloatField()
    linearaccelerationmin = models.FloatField()
    linearaccelerationmax = models.FloatField()
    linearaccelerationstd = models.FloatField()
    
    # Sensor data - Gravity
    gravitymagnitudemean = models.FloatField()
    gravitymagnitudemin = models.FloatField()
    gravitymagnitudemax = models.FloatField()
    gravitymagnitudestd = models.FloatField()
    gravitypitchmean = models.FloatField()
    gravitypitchmin = models.FloatField()
    gravitypitchmax = models.FloatField()
    gravitypitchstd = models.FloatField()
    gravityrollmean = models.FloatField()
    gravityrollmin = models.FloatField()
    gravityrollmax = models.FloatField()
    gravityrollstd = models.FloatField()
    
    # Sensor data - Magnetometer
    magneticfieldstrengthmean = models.FloatField()
    magneticfieldstrengthmin = models.FloatField()
    magneticfieldstrengthmax = models.FloatField()
    magneticfieldstrengthstd = models.FloatField()
    magneticfielduncalibratedhardironmean = models.FloatField()
    magneticfielduncalibratedhardironmin = models.FloatField()
    magneticfielduncalibratedhardironmax = models.FloatField()
    magneticfielduncalibratedhardironstd = models.FloatField()
    magneticfielduncalibratedsoftironmean = models.FloatField()
    magneticfielduncalibratedsoftironmin = models.FloatField()
    magneticfielduncalibratedsoftironmax = models.FloatField()
    magneticfielduncalibratedsoftironstd = models.FloatField()
    
    # Sensor data - Pressure
    pressuremean = models.FloatField()
    pressuremin = models.FloatField()
    pressuremax = models.FloatField()
    pressurestd = models.FloatField()
    
    # Activity data
    stepcountermean = models.FloatField()
    stepcountermin = models.FloatField()
    stepcountermax = models.FloatField()
    stepcounterstd = models.FloatField()

    transporttypeusedtonextpoint = models.CharField(max_length=100)
    registeredactivities = models.CharField(max_length=120)

    def __str__(self):
        return f"Point at ({self.latitude}, {self.longitude}) - {self.timestamp}"