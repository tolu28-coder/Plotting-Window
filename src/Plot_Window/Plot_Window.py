from Plot_Window.Plot_Window_view import PlotWindowView
from Plot_Window.Plot_Window_model import PlotWindowModel
from Plot_Window.Plot_Window_presenter import PlotWindowPresenter


class PlotWindow(object):

    def __init__(self, parent):
        self.view = PlotWindowView(parent)
        self.model = PlotWindowModel()
        self.presenter = PlotWindowPresenter(self.view, self.model)