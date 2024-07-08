from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets
from user_interface import UserInterface
import sys


app = QtWidgets.QApplication(sys.argv)

window = UserInterface()
window.show()
app.exec()

