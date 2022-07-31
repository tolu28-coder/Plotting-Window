import numpy as np



TEXT_FILE_FORMAT = ["txt", "csv"]


class PlotWindowModel(object):

    def __init__(self):
        pass

    def open_file(self, file_name, filetype, skiprow, columns):
        if filetype in TEXT_FILE_FORMAT:
            x, y = self.open_text_file(file_name, skiprow, columns)
        else:
            raise NotImplemented
        return x, y

    def open_text_file(self, file, skiprow, columns):
        data = np.loadtxt(file, skiprows=skiprow)
        x, y = data[:, columns[0]], data[:, columns[1]]
        return x, y