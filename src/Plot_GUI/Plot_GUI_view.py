import sys
import matplotlib
from qtpy import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from Plotting_object import SinglePlot
matplotlib.use('Qt5Agg')

class SingleMplCanvas(QtWidgets.QWidget):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        super(SingleMplCanvas, self).__init__(parent)
        self.plot_object = SinglePlot()
        self.axes = self.plot_object.axes
        self.canvas = FigureCanvas(self.plot_object.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        
    def plot(self, x, y, label=None):
        self.plot_object.plot(x, y, label)
        self.canvas.draw()
    
    def set_title(self, title):
        self.plot_object.set_title(title)
    
    def set_xlabel(self, label):
        pass

    def set_ylabel(self, label):
        pass

class MutliplotMplCanvas(QtWidgets.QWidget):
    
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        pass
    
    def plot(self, x, y, row, column, label):
        pass
    
    def set_title(self, title):
        pass
    
    def set_xlabel(self, label):
        pass

    def set_ylabel(self, label):
        pass 
    

if __name__ == '__main__':
    

    class MainWindow(QtWidgets.QMainWindow):
        
        def __init__(self, *args, **kwargs):
            super(MainWindow, self).__init__(*args, **kwargs)
            
            # Create the maptlotlib FigureCanvas object,
            # which defines a single set of axes as self.axes.
            sc = SingleMplCanvas(self, width=5, height=4, dpi=100)
            sc.plot([0,1,2,3,4], [10,1,20,3,40])
            sc.set_title("Title")
            self.setCentralWidget(sc)
            
            self.show()


    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()