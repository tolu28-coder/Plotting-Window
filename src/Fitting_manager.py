import numpy as np
from functions import FIT_FUNCTIONS
from Data_structures import FittedData
from scipy.optimize import curve_fit

## Add background to the fitting
class FittingManager(object):

    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.fitted_data = {}

    def fit(self, dataset_name, function, p0):
        func = FIT_FUNCTIONS[function]
        dataset = self.data_manager[dataset_name]
        x, y = dataset.get_data()
        popt, pcov = curve_fit(func, x, y, p0)
        # perr will be used later, error in fitting parameters
        perr = np.sqrt(np.diag(pcov))
        self.create_fitted_data(x, y, dataset_name, func, popt, perr)

    def create_fitted_data(self, x, y, dataset_name, func, popt, perr):
        fit = FittedData(x, y, dataset_name, func, popt, perr)
        self.fitted_data[dataset_name] = fit
        self.data_manager[dataset_name].fit = fit

    def __getitem__(self, label):
        return self.fitted_data[label]
