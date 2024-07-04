from PySide6.QtWidgets import QApplication, QPushButton

import sys

def button_clicked(data):
    print("clicked the button: ", data)


app = QApplication(sys.argv)
button = QPushButton("hi")
button.setCheckable(True)
button.clicked.connect(button_clicked)


button.show()

app.exec()