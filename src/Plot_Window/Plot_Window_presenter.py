from Plot_Window.Plot_Window_view import PlotWindowView
from Plot_Window.Plot_Window_model import PlotWindowModel


class PlotWindowPresenter(object):

    def __init__(self, view: PlotWindowView, model: PlotWindowModel):
        self.view = view
        self.model = model
        self._initialise_signals()

    def _initialise_signals(self):
        self.view.plot_data_slot(self.plot_data)
        self.view.fit_data_slot(self.fit_data)
        self.view.plot_custom_data_slot(self.plot_custom_data)
        self.view.remove_background_slot(self.remove_background)


    def plot_data(self):
        print("in plotting")

    def fit_data(self):
        print("in fitting")

    def plot_custom_data(self):
        print("in custom data")

    def remove_background(self):
        print("in remove background")

