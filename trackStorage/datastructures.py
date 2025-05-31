import queue
import pickle


class ReusableClassifier:
    def __init__(self, id):
        self.classifier = None
        with open("trackStorage/classifier.pkl", "rb") as file:
            self.classifier = pickle.load(file)
            
        self.id = id
        self.in_use = False
        self.feature_names = ['rotationmagnitudestd', 'rotationanglestd', 'gyroscopemagnitudestd', 'magneticfielduncalibratedhardironmax', 'gyroscopeturnratestd', 'gamerotationanglemax', 'magneticfielduncalibratedhardironmin', 'gravitymagnitudestd', 'gravityrollmin', 'gyroscopeuncalibratedmagnitudestd', 'gravitypitchstd', 'distance', 'gyroscopeuncalibratedmagnitudemin', 'stepcounterstd', 'gyroscopemagnitudemin', 'gyroscopemagnitudemax', 'gravitypitchmean', 'pressuremean', 'accelerometermin', 'magneticfieldstrengthmin', 'gamerotationmagnitudemax', 'gyroscopeturnratemin', 'linearaccelerationstd', 'speed', 'locationaccuracy', 'accelerometermax', 'gravityrollmax', 'magneticfieldstrengthmax', 'stepcountermean', 'gyroscopeturnratemean', 'magneticfielduncalibratedsoftironmin', 'linearaccelerationmax', 'gamerotationanglemin', 'gravitypitchmax', 'gamerotationanglestd', 'gyroscopeturnratemax', 'gravitymagnitudemean', 'magneticfielduncalibratedsoftironmax', 'linearaccelerationmean', 'pressuremax', 'speedaccuracy', 'magneticfieldstrengthmean', 'rotationanglemean', 'rotationanglemin', 'rotationanglemax', 'rotationmagnitudemax', 'accelerometermean', 'gamerotationmagnitudestd', 'magneticfielduncalibratedsoftironstd', 'gamerotationmagnitudemean', 'magneticfielduncalibratedhardironmean', 'rotationmagnitudemean', 'gyroscopeuncalibratedmagnitudemean', 'gravityrollstd', 'pressuremin', 'magneticfielduncalibratedhardironstd', 'magneticfielduncalibratedsoftironmean', 'gyroscopemagnitudemean', 'stepcountermax', 'gravitymagnitudemin', 'gravityrollmean', 'gyroscopeuncalibratedmagnitudemax', 'gamerotationanglemean', 'stepcountermin', 'accelerometerstd', 'gamerotationmagnitudemin', 'magneticfieldstrengthstd', 'rotationmagnitudemin', 'gravitymagnitudemax', 'gravitypitchmin', 'linearaccelerationmin', 'pressurestd', 'in_vehicle', 'on_bicycle', 'on_foot', 'running', 'still', 'tilting', 'unknown', 'walking']

    def acquire(self):
        if not self.in_use:
            self.in_use = True
            return True
        return False
    
    def release(self):
        self.in_use = False

    def predict(self, data: dict):
        x = [[data[feat] for feat in self.feature_names]]

        predictions = {str(k): float(v) for k, v in zip(self.classifier.classes_, self.classifier.predict_proba(x)[0])}
        return predictions


class ObjectPool:
    def __init__(self, size):
        self.size = size
        # For that reason: https://github.com/T-baby/pondpond
        # 20 consistent, 100 is max_size
        # self.max_size = max_size
        self.pool = queue.Queue(maxsize=size)
        self.initialize_pool()

    def initialize_pool(self):
        for i in range(self.size):
            self.pool.put(ReusableClassifier(i))

    def acquire(self):
        if not self.pool.empty():
            obj = self.pool.get()
            if obj.acquire():
                return obj
        return None

    def release(self, obj):
        obj.release()
        self.pool.put(obj)

    def __len__(self):
      return self.pool.qsize()
