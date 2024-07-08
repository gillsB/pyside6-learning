from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets
import sys

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load("widget.ui", None)


def do_something():
    print(window.fullname_line_edit.text(), "is a", window.occupation_line_edit.text())


window.setWindowTitle("QuiLoader")

window.submit_button.clicked.connect(do_something)
window.show()
app.exec()

