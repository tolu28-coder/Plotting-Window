from qtpy.QtWidgets import QMessageBox
from qtpy import QtWidgets
import sys

def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

def short_warning(text: str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()

class UserInput(QtWidgets.QWidget):

    def __init__(self, parent, text: str):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.label = QtWidgets.QLabel(self)
        self.layout.addWidget(self.label)
        self._initialise()
        self.setLayout(self.layout)
        self.set_label_text(text)

    def _initialise(self):
        raise NotImplemented

    def set_label_text(self, text):
        self.label.setText(text)

    def set_input(self, text):
        raise NotImplemented

    def get_input(self):
        raise NotImplemented


class UserInputText(UserInput):

    def _initialise(self):
        self.text_box = QtWidgets.QLineEdit(self)
        self.layout.addWidget(self.text_box)

    def set_input(self, text):
        self.text_box.setText(text)

    def get_input(self):
        return self.text_box.text()

class UserInputInt(UserInput):

    def _initialise(self):
        self.spinbox = QtWidgets.QSpinBox(self)
        self.layout.addWidget(self.spinbox)

    def set_input(self, integer):
        self.spinbox.setValue(integer)

    def get_input(self):
        return self.spinbox.value()

