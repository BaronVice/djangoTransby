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
        self.mean_values = {'rotationmagnitudestd': 0.02891421661746065, 'rotationanglestd': 0.11279328786498748, 'gyroscopemagnitudestd': 0.3208339914674827, 'magneticfielduncalibratedhardironmax': 74.73935286937444, 'gyroscopeturnratestd': 0.1497521735347804, 'gamerotationanglemax': 2.2058155151689394, 'magneticfielduncalibratedhardironmin': 74.11834316080308, 'gravitymagnitudestd': 9.143829221507131e-05, 'gravityrollmin': -26.63031513377619, 'gyroscopeuncalibratedmagnitudestd': 0.335623357462167, 'gravitypitchstd': 3.365104016008698, 'distance': 62.81350152517694, 'gyroscopeuncalibratedmagnitudemin': 0.16983519725199653, 'stepcounterstd': 0.07130307853793647, 'gyroscopemagnitudemin': 0.1595296980338552, 'gyroscopemagnitudemax': 1.267114644736081, 'gravitypitchmean': -1.1371907172589064, 'accelerometermin': 8.37979676292475, 'magneticfieldstrengthmin': 48.65465834208749, 'gamerotationmagnitudemax': 0.8372977753109063, 'gyroscopeturnratemin': 0.026516043802886594, 'linearaccelerationstd': 1.1320447404036822, 'speed': 7.628474442074608, 'locationaccuracy': 7.517609073673045, 'accelerometermax': 13.487508918984423, 'gravityrollmax': -0.924163939673251, 'magneticfieldstrengthmax': 57.83438410714893, 'stepcountermean': 0.46430393386851954, 'gyroscopeturnratemean': 0.17303005944163855, 'magneticfielduncalibratedsoftironmin': 95.50966325018648, 'linearaccelerationmax': 4.750360278508777, 'gamerotationanglemin': 1.8274333455409681, 'gravitypitchmax': 4.781666179310582, 'gamerotationanglestd': 0.1203248163183971, 'gyroscopeturnratemax': 0.5507104856623557, 'gravitymagnitudemean': 9.801955045689729, 'magneticfielduncalibratedsoftironmax': 106.03562570512781, 'linearaccelerationmean': 1.8650552586513496, 'speedaccuracy': 7.4635816800467785, 'magneticfieldstrengthmean': 53.118916276950635, 'rotationanglemean': 2.0761993864277932, 'rotationanglemin': 1.886413413638785, 'rotationanglemax': 2.254461559810015, 'rotationmagnitudemax': 0.8580643992836609, 'accelerometermean': 10.357826614138695, 'gamerotationmagnitudestd': 0.03252833899890226, 'magneticfielduncalibratedsoftironstd': 3.090938414321907, 'gamerotationmagnitudemean': 0.7909164083198077, 'magneticfielduncalibratedhardironmean': 74.38266666304152, 'rotationmagnitudemean': 0.8179728484394668, 'gyroscopeuncalibratedmagnitudemean': 0.5418736231769256, 'gravityrollstd': 8.248242947452633, 'magneticfielduncalibratedhardironstd': 0.23722586430218234, 'magneticfielduncalibratedsoftironmean': 100.86791836198402, 'gyroscopemagnitudemean': 0.5198413889567879, 'stepcountermax': 0.605406245145254, 'gravitymagnitudemin': 9.80173305349084, 'gravityrollmean': -14.74557856778053, 'gyroscopeuncalibratedmagnitudemax': 1.3643593446969142, 'gamerotationanglemean': 2.0133867587561776, 'stepcountermin': 0.39280720832686034, 'accelerometerstd': 1.4233287902955811, 'gamerotationmagnitudemin': 0.7363799138699378, 'magneticfieldstrengthstd': 2.684462855474083, 'rotationmagnitudemin': 0.7636579460448719, 'gravitymagnitudemax': 9.802063072439879, 'gravitypitchmin': -7.166655227802519, 'linearaccelerationmin': 0.6355294497047859, 'pressuremean': 959.029071009352, 'pressuremax': 959.0893144674404, 'pressuremin': 958.9703648058452, 'pressurestd': 0.03903739100294859}
        self.mean_values_len = len(self.mean_values)

        return super().ready()
