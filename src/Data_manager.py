import numpy as np
from Data_structures import Dataset


class DataManager(object):

    def __init__(self):
        self.datasets = {}

    def __getitem__(self, label):
        return self.datasets[label]

    @property
    def names_of_datasets(self):
        return list(self.datasets.keys())

    def add_dataset(self, x, y, label):
        dataset = Dataset(x, y, label)
        self.datasets[label] = dataset

    def remove_dataset(self, label):
        del self.datasets[label]

    def clear_data(self):
        self.datasets = {}

    def open_text_file(self, file, skiprow, columns, label):
        data = np.loadtxt(file, skiprows=skiprow)
        x, y = data[:, columns[0]], data[:, columns[1]]
        self.datasets[label] = Dataset(x, y, label)


