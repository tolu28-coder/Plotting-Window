from Plot_Window.Plot_Window_view import PlotWindowView
from Plot_Window.Plot_Window_model import PlotWindowModel
from UserInputWidgets.Large_user_input import PlotDataUserInput


class PlotWindowPresenter(object):

    def __init__(self, view, model):
        self.view = view
        self.model = model
        self._initialise_signals()
        self.setup_user_input()

    def setup_user_input(self):
        self.plot_large_input = None

    def _initialise_signals(self):
        self.view.plot_data_slot(self.plot_data)
        self.view.fit_data_slot(self.fit_data)
        self.view.plot_custom_data_slot(self.plot_custom_data)
        self.view.remove_background_slot(self.remove_background)

    def plot_data(self):
        if self.plot_large_input is not None:
            return
        self.plot_large_input = PlotDataUserInput()
        self.plot_large_input.done_button_slot(self.handle_plot_data)

    def handle_plot_data(self):
        parameters = self.plot_large_input.get_input()
        x, y = self.model.open_file(parameters["filename"], parameters["filetype"], parameters["row"], parameters["column"])
        label = parameters["label"]
        self.plot(x, y, label)
        self.model.add_dataset(x, y, label)
        self.plot_large_input = None


    def fit_data(self):
        print("in fitting")

    def plot_custom_data(self):
        print("in custom data")

    def remove_background(self):
        print("in remove background")

    def plot(self, x, y, label=""):
        self.view.plot(x, y, label)

