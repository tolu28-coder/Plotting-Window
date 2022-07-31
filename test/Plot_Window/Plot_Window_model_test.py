from Plot_Window.Plot_Window_model import PlotWindowModel
import unittest
import unittest.mock as mock
import time
from Common_directories import test_files_directory


class PlotWindowModelTest(unittest.TestCase):

    def setUp(self):
        self.model = PlotWindowModel()

    def test_open_file(self):
        mock_open_text_file = mock.Mock()
        mock_open_text_file.return_value = ["mock_x", "mock_y"]
        self.model.open_text_file = mock_open_text_file
        self.model.open_file("mock_file", "txt", "mock_row", "mock_column")
        time.sleep(1)
        mock_open_text_file.assert_called_once_with("mock_file", "mock_row", "mock_column")

    def test_open_file_that_is_not_text(self):
        with self.assertRaises(NotImplementedError):
            self.model.open_file("mock_file", "not_txt", "mock_row", "mock_column")

    def test_open_text_file(self):
        pass

    def test_add_dataset(self):
        pass
