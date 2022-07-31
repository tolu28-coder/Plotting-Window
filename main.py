from Plot_Window.Plot_Window import PlotWindow
from Misc import exception_hook
from qtpy.QtWidgets import QMainWindow, QApplication
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.plot_window = PlotWindow(self)
        self.setCentralWidget(self.plot_window.view)

        self.show()


sys._excepthook = sys.excepthook
sys.excepthook = exception_hook

app = QApplication(sys.argv)
w = MainWindow()
app.exec_()
