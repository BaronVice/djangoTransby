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
        self.mean_values = {'rotationmagnitudestd': 0.027879654679479008, 'rotationanglestd': 0.10782599585810511, 'gyroscopemagnitudestd': 0.307327093921438, 'magneticfielduncalibratedhardironmax': 64.30190515428801, 'gyroscopeturnratestd': 0.13783381970644398, 'gamerotationanglemax': 2.207799248695942, 'magneticfielduncalibratedhardironmin': 63.60120234124935, 'gravitymagnitudestd': 0.00012243191502539329, 'gravityrollmin': -25.982060281084127, 'gyroscopeuncalibratedmagnitudestd': 0.32256674715707384, 'gravitypitchstd': 3.1266412232107377, 'distance': 66.77929443406914, 'gyroscopeuncalibratedmagnitudemin': 0.15716051226950875, 'stepcounterstd': 0.06630874248074209, 'gyroscopemagnitudemin': 0.14595835265851687, 'gyroscopemagnitudemax': 1.2064947053293442, 'gravitypitchmean': -1.1580878021940255, 'accelerometermin': 8.407817021968066, 'magneticfieldstrengthmin': 49.22745381214052, 'gamerotationmagnitudemax': 0.8369721666186869, 'gyroscopeturnratemin': 0.022345919560341005, 'linearaccelerationstd': 1.073121006715538, 'speed': 7.905395417036463, 'locationaccuracy': 7.327211576267861, 'accelerometermax': 13.323681986366694, 'gravityrollmax': -0.6443720323822939, 'magneticfieldstrengthmax': 58.16883180737868, 'stepcountermean': 0.4499180549592691, 'gyroscopeturnratemean': 0.15445846615181535, 'magneticfielduncalibratedsoftironmin': 85.72381007257935, 'linearaccelerationmax': 4.467894306447698, 'gamerotationanglemin': 1.8417987064338401, 'gravitypitchmax': 4.367642470114934, 'gamerotationanglestd': 0.11636439058716859, 'gyroscopeturnratemax': 0.5057106668402197, 'gravitymagnitudemean': 9.800355536650885, 'magneticfielduncalibratedsoftironmax': 96.13459206004859, 'linearaccelerationmean': 1.7428705466953727, 'speedaccuracy': 7.660892568464684, 'magneticfieldstrengthmean': 53.44218882798827, 'rotationanglemean': 2.0974603346694836, 'rotationanglemin': 1.9168219160298465, 'rotationanglemax': 2.2711569741073436, 'rotationmagnitudemax': 0.8620994061874092, 'accelerometermean': 10.319360484126056, 'gamerotationmagnitudestd': 0.03203114706584443, 'magneticfielduncalibratedsoftironstd': 3.0386353798514922, 'gamerotationmagnitudemean': 0.7906034976976087, 'magneticfielduncalibratedhardironmean': 63.895480289135655, 'rotationmagnitudemean': 0.8227301159515611, 'gyroscopeuncalibratedmagnitudemean': 0.5115635261319325, 'gravityrollstd': 8.183563649193701, 'magneticfielduncalibratedhardironstd': 0.2622977577603518, 'magneticfielduncalibratedsoftironmean': 90.917191308353, 'gyroscopemagnitudemean': 0.48931482695059053, 'stepcountermax': 0.585459847932507, 'gravitymagnitudemin': 9.80005814616468, 'gravityrollmean': -14.110160695784884, 'gyroscopeuncalibratedmagnitudemax': 1.3070629623148147, 'gamerotationanglemean': 2.0205365016253563, 'stepcountermin': 0.38329340693677744, 'accelerometerstd': 1.370027104750937, 'gamerotationmagnitudemin': 0.7374653182558617, 'magneticfieldstrengthstd': 2.602999281471138, 'rotationmagnitudemin': 0.7703876180900775, 'gravitymagnitudemax': 9.800500102401699, 'gravitypitchmin': -6.801913744115432, 'linearaccelerationmin': 0.5848606025561119, 'pressuremean': 960.5514667803744, 'pressuremax': 960.6088356511867, 'pressuremin': 960.4954660270943, 'pressurestd': 0.037434694324727014}
        self.mean_values_len = len(self.mean_values)

        return super().ready()
