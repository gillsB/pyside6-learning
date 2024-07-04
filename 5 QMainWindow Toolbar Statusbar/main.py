from PySide6.QtWidgets import QApplication
from mainwindow import Window
import sys


app = QApplication(sys.argv)

window = Window(app)
window.show()

app.exec()