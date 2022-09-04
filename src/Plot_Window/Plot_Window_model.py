import numpy as np
from scipy.optimize import curve_fit
from Mythreads import MyThread, Messenger
from functions import FIT_FUNCTIONS
from Data_structures import Dataset
from Plot_Window.Data_manager import DataManager
from Plot_Window.Fitting_manager import FittingManager

TEXT_FILE_FORMAT = ["txt", "csv"]
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
            x, y = self.open_text_file(file_name, skiprow, columns)
        else:
            raise NotImplementedError
        return x, y, label

    @MyThread.thread_padding_return(0,  1,  0,  0)
    def fit_data(self, dataset_name, function, p0):
        func = FIT_FUNCTIONS[function]
        dataset = self.data_manager[dataset_name]
        x, y = dataset.get_data()
        popt, pcov = curve_fit(func, x, y, p0)
        # perr will be used later, error in fitting parameters
        perr = np.sqrt(np.diag(pcov))
        return x, func(x, *popt), popt, dataset_name + "_fitted_function"


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
