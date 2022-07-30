from qtpy import QtWidgets
from Misc import UserInputText, UserInputInt


class PlotDataUserInput(QtWidgets.QWidget):

    def __init__(self):
        self.file_type_label = QtWidgets.QLabel(self)
        self.file_type_combobox = QtWidgets.QComboBox(self)
        self.row_input = UserInputInt("Select number of rows to ignore")



