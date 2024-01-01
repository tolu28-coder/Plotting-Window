from Plot_Window.Plot_Window_view import PlotWindowView
from Plot_Window.Plot_Window_model import PlotWindowModel
from Plot_Window.Plot_Window_presenter import PlotWindowPresenter
from Data_manager_GUI.Data_Manger_GUI_View import DataManagerGUIView
from Data_manager import DataManager


class PlotWindow(object):

    def __init__(self, parent):
        self.view = PlotWindowView(parent)
        self.model = PlotWindowModel()
        self.presenter = PlotWindowPresenter(self.view, self.model)
