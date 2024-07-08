from PySide6 import QtCore, QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class UserInterface(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("widget.ui", None)
        self.ui.setWindowTitle("QUiLoader cleaner")
        self.ui.submit_button.clicked.connect(self.do_something)
    def show(self):
        self.ui.show()
    def do_something(self):
        print(self.ui.fullname_line_edit.text(),"is a", self.ui.occupation_line_edit.text())