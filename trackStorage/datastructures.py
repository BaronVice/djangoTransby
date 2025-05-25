import queue

class ReusableClassifier:
    def __init__(self, id):
        self.id = id
        self.in_use = False

    def acquire(self):
        if not self.in_use:
            self.in_use = True
            return True
        return False
    
    def release(self):
        self.in_use = False

    def predict(self, data):
        return {
            'confidence': 1.0,
            'mode': 'пешком'
        }


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