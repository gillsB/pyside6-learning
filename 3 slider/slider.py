from PySide6.QtWidgets import QApplication, QSlider
from PySide6.QtCore import Qt
import sys

def slider_changed(data):
    print("slider changed to", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)


slider.valueChanged.connect(slider_changed)
slider.show()
app.exec()