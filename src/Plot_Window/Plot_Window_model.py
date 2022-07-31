import numpy as np



TEXT_FILE_FORMAT = ["txt", "csv"]


class PlotWindowModel(object):

    def __init__(self):
        self.datasets = {}

    def open_file(self, file_name, filetype, skiprow, columns):
        if filetype in TEXT_FILE_FORMAT:
            x, y = self.open_text_file(file_name, skiprow, columns)
        else:
            raise NotImplementedError
        return x, y

    def open_text_file(self, file, skiprow, columns):
        data = np.loadtxt(file, skiprows=skiprow)
        x, y = data[:, columns[0]], data[:, columns[1]]
        return x, y

    def add_dataset(self, x, y, label):
        dataset = Dataset(x, y, label)
        self.datasets[label] = dataset

    def remove_dataset(self, label):
        if label in self.datasets:
            del self.datasets[label]

    def get_list_of_datasets_present(self):
        return list(self.datasets.keys())

    def get_dataset(self, label):
        return self.datasets[label]



class Dataset(object):

    def __init__(self, x, y, label):
        self.xdata = x
        self.ydata = y
        self.label = label

    def get_data(self):
        return self.xdata, self.ydata

    def __str__(self):
        return self.label