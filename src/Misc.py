from qtpy.QtWidgets import QMessageBox
import sys
from queue import Queue


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


def short_warning(text: str):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


class Executor(object):

    def __init__(self):
        self.output = Queue()

    def execute(self, code, **kwargs):
        kwargs["Output"] = self.output
        try:
            exec(code, kwargs)
        except Exception as E:
            print(short_warning(E))

    def get_output(self):
        return self.output.get()