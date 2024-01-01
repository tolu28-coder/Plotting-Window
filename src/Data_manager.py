import numpy as np
from Data_structures import Dataset
from collections import OrderedDict
from Mythreads import Messenger
from Misc import Executor


class DataManager(object):

    def __init__(self):
        self.datasets = OrderedDict()
        self.data_changed_messenger = Messenger()
        self.plot_index = []
        self.Open_executor = Executor()

    def __getitem__(self, label):
        return self.datasets[label]

    @property
    def names_of_datasets(self):
        return list(self.datasets.keys())

    def add_dataset(self, x, y, label):
        dataset = Dataset(x, y, label)
        self.datasets[label] = dataset
        #self.data_changed_messenger.notify()

    def remove_dataset(self, label):
        del self.datasets[label]
        self.data_changed_messenger.notify()

    def clear_data(self):
        self.datasets = {}
        self.data_changed_messenger.notify()

    def open_text_file(self, file, skiprow, columns, label):
        data = np.loadtxt(file, skiprows=skiprow)
        x, y = data[:, columns[0]], data[:, columns[1]]
        self.add_dataset(x, y, label)

    def open_csv_file(self, file, skiprow, columns, label):
        data = np.loadtxt(file, skiprows=skiprow, delimiter=",")
        x, y = data[:, columns[0]], data[:, columns[1]]
        self.add_dataset(x, y, label)



