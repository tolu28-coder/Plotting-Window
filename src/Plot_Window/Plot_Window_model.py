import numpy as np
from Mythreads import MyThread, Messenger

TEXT_FILE_FORMAT = ["txt", "csv"]


class PlotWindowModel(MyThread):

    def __init__(self):
        MyThread.__init__(self)
        self.datasets = {}
        self.open_file_messenger = Messenger()

    @MyThread.thread_padding_return
    def open_file(self, file_name, filetype, skiprow, columns, label):
        if filetype in TEXT_FILE_FORMAT:
            x, y = self.open_text_file(file_name, skiprow, columns)
        else:
            raise NotImplementedError
        return x, y, label


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

    def before_thread(self):
        #print("In before thread")
        pass

    def thread_success(self):
        self.open_file_messenger.notify()

    def incase_of_error(self, exception):
        print("here")
        raise exception

    def get_from_queue(self):
        return self._queue.get()

    def after_thread(self):
        pass

class Dataset(object):

    def __init__(self, x, y, label):
        self.xdata = x
        self.ydata = y
        self.label = label

    def get_data(self):
        return self.xdata, self.ydata

    def __str__(self):
        return self.label
