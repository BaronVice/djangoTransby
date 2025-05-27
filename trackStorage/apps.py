from django.apps import AppConfig
from trackStorage.datastructures import ObjectPool


class TrackstorageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trackStorage'

    def __init__(self, app_name, app_module):
        super().__init__(app_name, app_module)
        # Initialize mutable attributes in __init__
        self.model_pool = None
        self.mean_values = None
        self.mean_values_len = None

    def ready(self):
        self.model_pool = ObjectPool(size=5)
        self.mean_values = {'rotationmagnitudestd': 0.027891479146555542, 'rotationanglestd': 0.1080606523329328, 'gyroscopemagnitudestd': 0.3129081539213002, 'magneticfielduncalibratedhardironmax': 64.33062898595986, 'gyroscopeturnratestd': 0.14092299411246048, 'gamerotationanglemax': 2.2062957359409014, 'magneticfielduncalibratedhardironmin': 63.63255812135781, 'gravitymagnitudestd': 0.00011990773009989264, 'gravityrollmin': -26.350338045218574, 'gyroscopeuncalibratedmagnitudestd': 0.3279145380697635, 'gravitypitchstd': 3.147999636586336, 'distance': 66.13998325297261, 'gyroscopeuncalibratedmagnitudemin': 0.16147387585333065, 'stepcounterstd': 0.06807780985503405, 'gyroscopemagnitudemin': 0.14953258317258164, 'gyroscopemagnitudemax': 1.229544632228529, 'gravitypitchmean': -1.5688764588478414, 'accelerometermin': 8.389561625301042, 'magneticfieldstrengthmin': 49.21766886820543, 'gamerotationmagnitudemax': 0.8370257088446715, 'gyroscopeturnratemin': 0.02275861053476927, 'linearaccelerationstd': 1.09054533445325, 'speed': 7.860477210580477, 'locationaccuracy': 7.249547394438272, 'accelerometermax': 13.375709749865365, 'gravityrollmax': -0.875954560848178, 'magneticfieldstrengthmax': 58.19446859014454, 'stepcountermean': 0.4584196443565777, 'gyroscopeturnratemean': 0.1582168744814796, 'magneticfielduncalibratedsoftironmin': 85.35530964917275, 'linearaccelerationmax': 4.548511257303203, 'gamerotationanglemin': 1.8413597610580352, 'gravitypitchmax': 3.9677664829928063, 'gamerotationanglestd': 0.1159213337709736, 'gyroscopeturnratemax': 0.51694008932322, 'gravitymagnitudemean': 9.800485867024065, 'magneticfielduncalibratedsoftironmax': 95.81025263247959, 'linearaccelerationmean': 1.7819135664275754, 'speedaccuracy': 7.787142371431166, 'magneticfieldstrengthmean': 53.44768443966827, 'rotationanglemean': 2.0942805305836467, 'rotationanglemin': 1.913590364526978, 'rotationanglemax': 2.2683834454133036, 'rotationmagnitudemax': 0.8612534550502554, 'accelerometermean': 10.323812747735438, 'gamerotationmagnitudestd': 0.031860987947321597, 'magneticfielduncalibratedsoftironstd': 3.0604491864260166, 'gamerotationmagnitudemean': 0.7908877161058422, 'magneticfielduncalibratedhardironmean': 63.92557212133958, 'rotationmagnitudemean': 0.8218466512724636, 'gyroscopeuncalibratedmagnitudemean': 0.5226687109843052, 'gravityrollstd': 8.230368327665825, 'magneticfielduncalibratedhardironstd': 0.26222231995282846, 'magneticfielduncalibratedsoftironmean': 90.5796599487904, 'gyroscopemagnitudemean': 0.500005191018022, 'stepcountermax': 0.5968992248062015, 'gravitymagnitudemin': 9.800194620077006, 'gravityrollmean': -14.432212586923281, 'gyroscopeuncalibratedmagnitudemax': 1.330226023591559, 'gamerotationanglemean': 2.0196282842964375, 'stepcountermin': 0.38994288045695635, 'accelerometerstd': 1.3905287778080697, 'gamerotationmagnitudemin': 0.7379362001748683, 'magneticfieldstrengthstd': 2.6181455883059055, 'rotationmagnitudemin': 0.7696023575187466, 'gravitymagnitudemax': 9.800627459244483, 'gravitypitchmin': -7.258867615901241, 'linearaccelerationmin': 0.6035034275068989, 'pressuremean': 959.9516370817043, 'pressuremax': 960.0089427973852, 'pressuremin': 959.8956013771758, 'pressurestd': 0.03738390657621159}
        self.mean_values_len = len(self.mean_values)

        return super().ready()
