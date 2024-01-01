from Data_manager_GUI.Data_Manger_GUI_View import DataManagerGUIView
from Data_manager import DataManager
from Data_structures import Dataset
from Mythreads import Messenger




class DataManagerPresenter(object):

    def __init__(self, view, datamanager):
        self.view = view
        self.datamanager = datamanager

        self.datamanager.data_changed_messenger.setup(self.update_table)
        self.view.on_plot_checkbox_messenger.setup(self.on_plot_checkbox_changed)
        self.view.on_plot_fitted_checkbox_messenger.setup(self.on_plot_fitted_checkbox_changed)

        self.on_plot_checkbox_messenger = Messenger()
        self.remove_line_messenger = Messenger()
        self.plot_line_messenger = Messenger()

    def update_table(self):
        self.view.clear_table()
        for name in self.datamanager.names_of_datasets:
            dataset = self.datamanager[name]
            self.add_row(dataset)

    def add_row(self, dataset):
        self.view.add_row(dataset)

    def on_plot_checkbox_changed(self, row, state):
        # pull out dataset name and state of checkbox from the view
        dataset_name = self.view.index_table(row, 0).text()
        if state:
            dataset = self.datamanager[dataset_name]

            self.plot_line_messenger.notify_with_args(dataset.xdata, dataset.ydata, dataset_name)
        else:
            self.remove_line_messenger.notify_with_args(dataset_name)

    def on_plot_fitted_checkbox_changed(self, row, state):
        dataset_name = self.view.index_table(row, 0).text()
        dataset = self.datamanager[dataset_name].fitted_data
        if state:
            self.plot_line_messenger.notify_with_args(dataset.xdata, dataset.ydata, dataset.plot_label)
        else:
            self.remove_line_messenger.notify_with_args(dataset.plot_label)