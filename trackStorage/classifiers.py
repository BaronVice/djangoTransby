import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import LabelEncoder

class ProbabilisticNeuralNetwork:
    def __init__(self, sigma=1.0):
        self.sigma = sigma  # Smoothing parameter
        self.classes = None
        self.class_means = {}
        self.class_stds = {}
        self.label_encoder = LabelEncoder()
        self.feature_names = None

    def fit(self, X, y):
        X = np.array(X, dtype=np.float64)

        y_encoded = self.label_encoder.fit_transform(y)
        self.classes = self.label_encoder.classes_

        for cls in np.unique(y_encoded):
            cls_mask = (y_encoded == cls)
            self.class_means[cls] = np.mean(X[cls_mask], axis=0)
            self.class_stds[cls] = np.std(X[cls_mask], axis=0)

    def _calculate_probability(self, x, mean, std):
        return np.prod(norm.pdf(x, mean, std + self.sigma))

    def predict_proba(self, X):
        X = np.array(X, dtype=np.float64)  # Ensure numeric
        probabilities = np.zeros((len(X), len(self.classes)))

        for cls in self.class_means:
            cls_idx = self.label_encoder.transform([cls])[0]
            for i, x in enumerate(X):
                prob = self._calculate_probability(
                    x,
                    self.class_means[cls],
                    self.class_stds[cls]
                )
                probabilities[i, cls_idx] = prob

        probabilities /= probabilities.sum(axis=1, keepdims=True)
        return probabilities

    def predict(self, X):
        proba = self.predict_proba(X)
        return [self.label_encoder.inverse_transform(np.argmax(proba, axis=1)), proba]
        # return self.label_encoder.inverse_transform(np.argmax(proba, axis=1))