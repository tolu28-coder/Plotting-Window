from Plot_Window.Plot_Window_presenter import PlotWindowPresenter
import unittest
import unittest.mock as mock


class PlotWindowPresenterTest(unittest.TestCase):

    def setUp(self):
        self.presenter = PlotWindowPresenter(mock.Mock(), mock.Mock())

    @mock.patch("Plot_Window.Plot_Window_presenter.PlotDataUserInput")
    def test_plot_data_creates_gui(self, mock_user_input):
        self.presenter.plot_data()
        mock_user_input.assert_called_once()

    def test_handle_plot_data_calls_on_model(self):
        mock_params = {"filetype": "mock_filetype", "filename": "mock_file", "row": "mock_row", "column": "mock_column",
                       "label": "mock_label"}
        mock_data = [0, 1]
        self.presenter.model.open_file.return_value = mock_data
        self.presenter.plot_large_input = mock.Mock()
        self.presenter.plot_large_input.get_input.return_value = mock_params
        self.presenter.handle_plot_data()
        self.presenter.model.open_file.assert_called_once_with("mock_file", "mock_filetype", "mock_row", "mock_column")
        self.presenter.view.plot.assert_called_once_with(0, 1, "mock_label")
        self.presenter.model.add_dataset.assert_called_once_with(0, 1, "mock_label")


if __name__ == '__main__':
    unittest.main()
