from qtpy import QtWidgets, QtCore
from Plot_GUI.Plot_GUI_view import SingleMplCanvas


class PlotWindowView(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(PlotWindowView, self).__init__(parent)
        self.overall_layout = QtWidgets.QVBoxLayout(self)
        self._createMenuBar()
        self.plot_canvas = SingleMplCanvas(self)
        self.overall_layout.addWidget(self.menuBar)
        self.overall_layout.addWidget(self.plot_canvas)


    def plot_data_slot(self, slot):
        self.plot_action.triggered.connect(slot)

    def fit_data_slot(self, slot):
        self.fit_action.triggered.connect(slot)

    def plot_custom_data_slot(self, slot):
        self.custom_plot_action.triggered.connect(slot)

    def remove_background_slot(self, slot):
        self.remove_background.triggered.connect(slot)

    def _createMenuBar(self):
        self.menuBar = QtWidgets.QMenuBar()
        # Creating menus using a QMenu object
        self.plot_menu = self.menuBar.addMenu("&Plotting")
        self.plot_action = QtWidgets.QAction("Plot data", self)
        self.plot_action.setStatusTip('Add data to plot')
        #self.plot_action.triggered.connect(self.handle_plot_data)
        self.plot_menu.addAction(self.plot_action)

        self.custom_plot_action = QtWidgets.QAction("&Custom data", self)
        self.custom_plot_action.setStatusTip('Plot custom data')
        #self.custom_plot_action.triggered.connect(self.handle_custom_plot_data)
        self.plot_menu.addAction(self.custom_plot_action)

        # Creating menus using a title
        self.fit_menu = self.menuBar.addMenu("&Fitting")
        self.fit_action = QtWidgets.QAction("Fit data", self)
        self.fit_action.setStatusTip('Fit plotted data')
        #fit_action.triggered.connect(self.plot_data)
        self.fit_menu.addAction(self.fit_action)

        self.correct_menu = self.menuBar.addMenu("&Corrections")
        self.remove_background = QtWidgets.QAction("Remove background")
        self.remove_background.setStatusTip("Remove background from data")
        self.correct_menu.addAction(self.remove_background)

        self.add_lines_menu = self.menuBar.addMenu("&Add lines")





    def open_file(self):
        pass

    def plot(self):
        pass
