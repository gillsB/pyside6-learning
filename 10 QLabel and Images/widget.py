from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PySide6.QtGui import QPixmap


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel and images")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("gnome.png"))

        layout = QVBoxLayout()
        layout.addWidget(image_label)
        self.setLayout(layout)