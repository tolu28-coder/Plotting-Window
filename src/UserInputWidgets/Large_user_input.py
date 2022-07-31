from qtpy import QtWidgets

from UserInputWidgets.User_inputs import UserInputFileDirectory, UserInputInt, UserInputCombobox, UserInputText

ALLOWED_FILE_TYPES = ["txt", "csv"]


class LargeInput(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(LargeInput, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self._initialise()
        self.done_button = QtWidgets.QPushButton(self)
        self.done_button.setText("Done")
        self.layout.addWidget(self.done_button)
        self.setLayout(self.layout)
        self.show()
        self.done_button.clicked.connect(self.close)

    def _initialise(self):
        raise NotImplementedError

    def get_input(self):
        raise NotImplementedError

    def done_button_slot(self, slot):
        self.done_button.clicked.connect(slot)


class PlotDataUserInput(LargeInput):

    def _initialise(self):
        self.file_type_input = UserInputCombobox(self, "Select File type")
        self.file_type_input.add_options(ALLOWED_FILE_TYPES)
        self.label_input = UserInputText(self, "Plot label")
        self.row_input = UserInputInt(self, "Select number of rows to ignore")
        self.x_column_input = UserInputInt(self, "Select x column index")
        self.y_column_input = UserInputInt(self, "Select y column index")
        self.file_input = UserInputFileDirectory(self)

        self.layout.addWidget(self.file_type_input)
        self.layout.addWidget(self.file_input)
        self.layout.addWidget(self.label_input)
        self.layout.addWidget(self.row_input)
        self.layout.addWidget(self.x_column_input)
        self.layout.addWidget(self.y_column_input)

    def get_input(self):
        parameters = {"filetype": self.file_type_input.get_input(), "filename": self.file_input.get_input(),
                      "row": self.row_input.get_input(),
                      "column": (self.x_column_input.get_input(), self.y_column_input.get_input()),
                      "label": self.label_input.get_input()}
        return parameters
