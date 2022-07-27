from qtpy.QtWidgets import QWidget, QMenu, QAction
from Plot_GUI.Plot_GUI_view import SingleMplCanvas


class PlotWindow(QWidget):

    def __init__(self, parent=None):
        super(PlotWindow, self).__init__(parent)
        self.plot = SingleMplCanvas(self)

    def _createMenuBar(self):
        self.menuBar = self.menuBar()
        # Creating menus using a QMenu object
        plot_menu = QMenu("&Plot", self)
        plot_action = QAction("Plot data")
        plot_action.setStatusTip('Add data to plot')
        plot_action.triggered.connect(self.handle_plot_data)

        custom_plot_action = QAction("&Custom data")
        custom_plot_action.setStatusTip('Plot custom data')
        custom_plot_action.triggered.connect(self.handle_custom_plot_data)

        self.menuBar.addMenu(plot_menu)
        # Creating menus using a title
        fit_menu = self.menuBar.addMenu("&Fit")
        fit_action = QAction("Fit data")
        #fit_action.setStatusTip('Add data to plot')
        fit_action.triggered.connect(self.plot_data)

        helpMenu = self.menuBar.addMenu("&Add lines")

    def open_file(self):
        pass

    def plot_data(self):
        pass

    def custom_plot_data(self):
        pass

    def handle_plot_data(self):
        pass

    def handle_custom_plot_data(self):
        pass
