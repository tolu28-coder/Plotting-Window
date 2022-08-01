from UserInputWidgets.Large_user_input import PlotDataUserInput, FitDataUserInput


class PlotWindowPresenter(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self._initialise_signals()
        self.setup_user_input()
        self.setup_messengers()

    def setup_messengers(self):
        self.model.open_file_messenger.setup(self.open_file_done)
        self.model.fit_data_messenger.setup(self.fit_data_done)

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
        x, y, label = self.model.get_from_queue()
        self.plot(x, y, label)
        self.model.add_dataset(x, y, label)

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
        x, y, popt, label = self.model.get_from_queue()
        # popt not yet used
        self.plot(x, y, label)

    def plot_custom_data(self):
        print("in custom data")

    def remove_background(self):
        print("in remove background")

    def plot(self, x, y, label=""):
        self.view.plot(x, y, label)

