from qtpy.QtWidgets import QMessageBox
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

