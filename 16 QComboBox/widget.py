from PySide6.QtWidgets import QWidget, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QComboBox")


        self.combo_box = QComboBox(self)

        self.combo_box.addItem("Earth")
        self.combo_box.addItem("Venus")
        self.combo_box.addItem("Mars")
        self.combo_box.addItem("Saturn")
        self.combo_box.addItem("Jupiter")

        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.current_value)
        button_set_value = QPushButton("Set Value")
        button_set_value.clicked.connect(self.set_value)
        button_get_value = QPushButton("Get Value")
        button_get_value.clicked.connect(self.get_value)


        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(button_current_value)
        v_layout.addWidget(button_set_value)
        v_layout.addWidget(button_get_value)

        self.setLayout(v_layout)




    def current_value(self):
        print("Current value : ", self.combo_box.currentText(), " - current index : ", self.combo_box.currentIndex())
    def set_value(self):
        self.combo_box.setCurrentIndex(2)
    def get_value(self):
        for i in range(self.combo_box.count()):
            print("index [", i, "]: ", self.combo_box.itemText(i))