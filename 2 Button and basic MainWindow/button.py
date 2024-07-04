from PySide6.QtWidgets import QMainWindow, QPushButton


class Button(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button")
        button = QPushButton("hi")
        self.setCentralWidget(button)
