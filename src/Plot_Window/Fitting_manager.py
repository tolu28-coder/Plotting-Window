import numpy as np
from scipy.optimize import curve_fit


class FittingManager(object):

    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.fitted_data = {}

    def fit(self, dataset, function, p0):
        pass

    def __getitem__(self, label):
        return self.fitted_data[label]
