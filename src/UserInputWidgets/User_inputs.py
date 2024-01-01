from qtpy import QtWidgets
from qtpy.QtWidgets import QFileDialog


class UserInput(QtWidgets.QWidget):

    def __init__(self, parent=None, text: str = ""):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.label = QtWidgets.QLabel(self)
        self.layout.addWidget(self.label)
        self._initialise()
        self.setLayout(self.layout)
        self.set_label_text(text)

    def _initialise(self):
        raise NotImplementedError

    def set_label_text(self, text):
        self.label.setText(text)

    def set_input(self, text):
        raise NotImplementedError

    def get_input(self):
        raise NotImplementedError


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


class UserInputCombobox(UserInput):

    def _initialise(self):
        self.combobox = QtWidgets.QComboBox(self)
        self.layout.addWidget(self.combobox)

    def add_options(self, values):
        self.combobox.addItems(values)

    def set_input(self, index):
        self.combobox.setCurrentIndex(index)

    def get_input(self):
        return self.combobox.currentText()

    def index_changed_signal(self, function):
        self.combobox.currentIndexChanged.connect(function)


class UserInputFileDirectory(UserInputText):

    def __init__(self, parent):
        super(UserInputFileDirectory, self).__init__(parent, "Select file: ")

    def _initialise(self):
        super(UserInputFileDirectory, self)._initialise()
        self.button = QtWidgets.QPushButton(self)
        self.button.setText("Pick file")
        self.button.clicked.connect(self.button_clicked)
        self.layout.addWidget(self.button)

    def button_clicked(self):
        file = QFileDialog.getOpenFileName()
        self.set_input(file[0])






