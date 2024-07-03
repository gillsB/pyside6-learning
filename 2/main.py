from PySide6.QtWidgets import QApplication
from button import Button

import sys

app = QApplication(sys.argv)

window = Button()
window.show()

app.exec()