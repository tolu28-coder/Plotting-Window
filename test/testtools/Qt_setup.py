from qtpy.QtWidgets import QApplication
from Misc import exception_hook
import sys

_QAPP = QApplication.instance()
#sys._excepthook = sys.excepthook
#sys.excepthook = exception_hook

def setup_qapp(cls):
    def empty_setup(_):
        pass

    def setUpClass(cls):
        sys.excepthook = exception_hook
        global _QAPP
        if _QAPP is None:
            _QAPP = QApplication([""])
        setUpClass_orig()

    setUpClass_orig = cls.setUpClass if hasattr(cls, 'setUpClass') else empty_setup
    setattr(cls, 'setUpClass', classmethod(setUpClass))
    return cls