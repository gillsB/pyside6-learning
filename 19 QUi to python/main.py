from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets
from widget import Widget

import sys


app = QtWidgets.QApplication(sys.argv)

window = Widget()
window.show()
app.exec()

