from qtpy import QtWidgets
from functions import FIT_FUNCTIONS
from UserInputWidgets.User_inputs import UserInputFileDirectory, UserInputInt, UserInputCombobox, UserInputText

ALLOWED_FILE_TYPES = ["txt", "csv"]


class LargeInput(QtWidgets.QWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super(LargeInput, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self._initialise(*args, **kwargs)
        self.done_button = QtWidgets.QPushButton(self)
        self.done_button.setText("Done")
        self.layout.addWidget(self.done_button)
        self.setLayout(self.layout)
        self.show()
        self.done_button.clicked.connect(self.close)

    def _initialise(self, *args, **kwargs):
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


class FitDataUserInput(LargeInput):

    def _initialise(self, available_datasets):
        self.datasets_input = UserInputCombobox(self, "Select dataset to fit")
        self.datasets_input.add_options(available_datasets)
        self.function_input = UserInputCombobox(self, "Select function")
        self.function_input.add_options(FIT_FUNCTIONS.keys())
        self.function_input.index_changed_signal(lambda i: self.function_input_changed())
        self.function_description_label = QtWidgets.QLabel(self)
        self.range_min_input = UserInputText(self, "Input beginning of fit range")
        self.range_max_input = UserInputText(self, "Input end of fit range")
        self.intial_param_input = UserInputText(self, "Intial guess for fitting parameters")
        self.function_input_changed()

        self.layout.addWidget(self.datasets_input)
        self.layout.addWidget(self.function_input)
        self.layout.addWidget(self.function_description_label)
        self.layout.addWidget(self.range_min_input)
        self.layout.addWidget(self.range_max_input)
        self.layout.addWidget(self.intial_param_input)


    def get_input(self):
        initial = self.intial_param_input.get_input()
        initial = [float(x) if x else 0 for x in initial.split(",")]
        parameters = {"dataset": self.datasets_input.get_input(), "function": self.function_input.get_input(),
                      "range": [self.range_min_input.get_input(), self.range_max_input.get_input()],
                      "initial": initial}
        return parameters

    def function_input_changed(self):
        function_name = self.function_input.get_input()
        function = FIT_FUNCTIONS[function_name]
        text = function.get_description()
        self.function_description_label.setText(text)

