from qtpy import QtWidgets, QtCore
from Mythreads import Messenger


TABLE_COLUMNS = ["DATASET", "PLOT", "IS FITTED", "PLOT FITTED", "FUNCTION", "PARAMETERS", "ERRORS"]


class DataManagerGUIView(QtWidgets.QWidget):

    def __init__(self, parent):
        super(DataManagerGUIView, self).__init__(parent)
        self.table = QtWidgets.QTableWidget(self)

        self.table.itemClicked.connect(self.handle_item_clicked)

        self.table.setColumnCount(len(TABLE_COLUMNS))
        self.table.setHorizontalHeaderLabels(TABLE_COLUMNS)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        vertical_headers = self.table.verticalHeader()
        vertical_headers.setSectionsMovable(False)
        vertical_headers.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        vertical_headers.setVisible(True)
        self.on_plot_checkbox_messenger = Messenger()
        self.on_plot_fitted_checkbox_messenger = Messenger()
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)
        self.resize(500, 500)
        # setup table with column

        # setup

    def add_row(self, dataset):

        count = self.table.rowCount()
        self.table.insertRow(count)
        # creating all cells in row one by one

        # Dataset
        table_item = QtWidgets.QTableWidgetItem(str(dataset))
        self.table.setItem(count, 0, table_item)

        # Plot
        is_plotted = dataset.is_plotted
        table_item = QtWidgets.QTableWidgetItem(is_plotted)
        if is_plotted:
            table_item.setCheckState(QtCore.Qt.Checked)
        else:
            table_item.setCheckState(QtCore.Qt.Unchecked)
        self.table.setItem(count, 1, table_item)

        # Is fitted
        if dataset.is_fitted:
            table_item = QtWidgets.QTableWidgetItem("Yes")
        else:
            table_item = QtWidgets.QTableWidgetItem("No")

        self.table.setItem(count, 2, table_item)

        # Plot_fitted
        is_plotted = dataset.is_plot_fitted
        if dataset.is_fitted:
            table_item = QtWidgets.QTableWidgetItem(is_plotted)
            if is_plotted:
                table_item.setCheckState(QtCore.Qt.Checked)
            else:
                table_item.setCheckState(QtCore.Qt.Unchecked)
        else:
            table_item = QtWidgets.QTableWidgetItem("N/A")
        self.table.setItem(count, 3, table_item)

        # Function
        function = str(dataset.fit.function) if dataset.is_fitted else "N/A"
        table_item = QtWidgets.QTableWidgetItem(function)
        self.table.setItem(count, 4, table_item)

        # Parameters
        parameters = str(dataset.fit.get_parameters()) if dataset.is_fitted else "N/A"
        table_item = QtWidgets.QTableWidgetItem(parameters)
        self.table.setItem(count, 5, table_item)

        # Errors
        error = str(dataset.fit.get_errors()) if dataset.is_fitted else "N/A"
        table_item = QtWidgets.QTableWidgetItem(error)
        self.table.setItem(count, 6, table_item)


    def handle_item_clicked(self, item):
        row, column = item.row(), item.column()
        if column == 1:
            state = self.index_table(row, column).checkState()
            self.on_plot_checkbox_messenger.notify_with_args(row, state)

        if column == 3:
            state = self.index_table(row, column).checkState()
            self.on_plot_fitted_checkbox_messenger.notify_with_args(row, state)

    def add_plot_cell(self, row):
        pass

    def add_plot_fitted_cell(self, row):
        pass


    def update_table(self):
        pass


    def on_plot_checkbox_changed(self):
        pass

    def index_table(self, row, column):
        return self.table.item(row, column)

    def clear_table(self):
        for index in reversed(range(self.table.rowCount())):
            self.table.removeRow(index)
