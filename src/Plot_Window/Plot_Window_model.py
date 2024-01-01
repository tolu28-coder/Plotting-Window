import numpy as np
from Mythreads import MyThread, Messenger
from Data_manager import DataManager
from Fitting_manager import FittingManager


TEXT_FILE_FORMAT = ["txt"]#, "csv"]
NUMBER_OF_AFTER_THREAD_METHODS = 1
NUMBER_OF_BEFORE_THREAD_METHODS = 1
NUMBER_OF_IF_ERROR_THREAD_METHODS = 1
NUMBER_OF_IF_SUCCESS_THREAD_METHODS = 2


class PlotWindowModel(MyThread):

    _execute_after_thread = [MyThread._null] * NUMBER_OF_AFTER_THREAD_METHODS
    _execute_before_thread = [MyThread._null] * NUMBER_OF_BEFORE_THREAD_METHODS
    _execute_if_error = [MyThread._null] * NUMBER_OF_IF_ERROR_THREAD_METHODS
    _execute_if_success = [MyThread._null] * NUMBER_OF_IF_SUCCESS_THREAD_METHODS

    def __init__(self):
        MyThread.__init__(self)
        self.data_manager = DataManager()
        self.fitting_manager = FittingManager(self.data_manager)
        self.setup_messengers()

    def setup_messengers(self):
        self.open_file_messenger = Messenger()
        self.fit_data_messenger = Messenger()

    @MyThread.thread_padding_return(0,  0,  0,  0)
    def open_file(self, file_name, filetype, skiprow, columns, label):
        if filetype in TEXT_FILE_FORMAT:
            self.data_manager.open_text_file(file_name, skiprow, columns, label)

        elif filetype == "csv":
            self.data_manager.open_csv_file(file_name, skiprow, columns, label)
        else:
            raise NotImplementedError
        return label

    @MyThread.thread_padding_return(0,  1,  0,  0)
    def fit_data(self, dataset_name, function, p0):
        self.fitting_manager.fit(dataset_name, function, p0)
        return dataset_name


    def open_text_file(self, file, skiprow, columns):
        data = np.loadtxt(file, skiprows=skiprow)
        x, y = data[:, columns[0]], data[:, columns[1]]
        return x, y

    def add_dataset(self, x, y, label):
        self.data_manager.add_dataset(x, y, label)

    def remove_dataset(self, label):
        self.data_manager.remove_dataset(label)

    def get_list_of_datasets_present(self):
        return self.data_manager.names_of_datasets

    def get_dataset(self, label):
        return self.data_manager[label]

    def get_fitted_data(self, label):
        return self.fitting_manager[label]

    @MyThread.add_to_list(_execute_before_thread, 0)
    def before_thread(self):
        pass

    @MyThread.add_to_list(_execute_if_success, 0)
    def open_file_success(self):
        self.open_file_messenger.notify()

    @MyThread.add_to_list(_execute_if_error, 0)
    def incase_of_error(self, exception):
        raise exception

    @MyThread.add_to_list(_execute_if_success,1)
    def fit_data_success(self):
        self.fit_data_messenger.notify()

    def get_from_queue(self):
        return self._queue.get()

    @MyThread.add_to_list(_execute_after_thread, 0)
    def after_thread(self):
        pass
