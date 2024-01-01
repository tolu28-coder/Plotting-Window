from UserInputWidgets.Large_user_input import PlotDataUserInput, FitDataUserInput
from Data_manager_GUI.Data_Manager_GUI_presenter import DataManagerPresenter



class PlotWindowPresenter(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.data_manager_presenter = DataManagerPresenter(self.view.data_manager_gui, self.model.data_manager)
        self.plot_index = {}
        self._initialise_signals()
        self.setup_user_input()
        self.setup_messengers()

    def setup_messengers(self):
        self.model.open_file_messenger.setup(self.open_file_done)
        self.model.fit_data_messenger.setup(self.fit_data_done)

        self.data_manager_presenter.plot_line_messenger.setup(self.plot)
        self.data_manager_presenter.remove_line_messenger.setup(self.remove_line)

    def setup_user_input(self):
        self.plot_large_input = None
        self.fit_large_input = None

    def _initialise_signals(self):
        self.view.plot_data_slot(self.plot_data)
        self.view.fit_data_slot(self.fit_data)
        self.view.plot_custom_data_slot(self.plot_custom_data)
        self.view.remove_background_slot(self.remove_background)

    def plot_data(self):
        if self.plot_large_input is not None:
            # make active
            return
        self.plot_large_input = PlotDataUserInput()
        self.plot_large_input.done_button_slot(self.call_handle_plot)

    def call_handle_plot(self):
        parameters = self.plot_large_input.get_input()
        label = parameters["label"]
        self.model.open_file(parameters["filename"], parameters["filetype"], parameters["row"], parameters["column"],
                             label)
        self.plot_large_input = None

    def open_file_done(self):
        label = self.model.get_from_queue()
        dataset= self.model.get_dataset(label)
        x, y = dataset.get_data()
        self.plot(x, y, label)
        self.data_manager_presenter.add_row(dataset)

    def fit_data(self):
        if self.fit_large_input is not None:
            return
        self.fit_large_input = FitDataUserInput(None, self.model.get_list_of_datasets_present())
        self.fit_large_input.done_button_slot(self.call_handle_fit)

    def call_handle_fit(self):
        parameters = self.fit_large_input.get_input()
        # range_min and range_max not yet implemented
        self.model.fit_data(parameters["dataset"], parameters["function"], parameters["initial"])
        self.fit_large_input = None

    def fit_data_done(self):
        name = self.model.get_from_queue()
        fitted_data = self.model.get_fitted_data(name)
        x, y = fitted_data.get_data()
        label = fitted_data.plot_label
        # popt not yet used
        self.plot(x, y, label)
        self.model.data_manager[name].plot_fitted = True
        self.data_manager_presenter.update_table()

    def plot_custom_data(self):
        print("in custom data")

    def remove_background(self):
        print("in remove background")

    def plot(self, x, y, label=""):
        self.plot_index[label] = self.view.plot(x, y, label)[0]

    def remove_line(self, label):
        line = self.plot_index[label]
        del self.plot_index[label]
        self.view.remove_line(line)


