from PySide6.QtWidgets import QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QPushButton


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QGridLayout")

        button_1 = QPushButton("One")
        button_2 = QPushButton("two")
        button_3 = QPushButton("three")
        
        button_4 = QPushButton("four")
        button_5 = QPushButton("five")
        button_6 = QPushButton("six")
        button_7 = QPushButton("seven")


        #reminder that the SizePolicy default is only Expanding on horizontal
        #thus the button without the following line would still only be vertical 1
        #just sitting in the middle of the two rows
        button_3.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)


        grid_layout = QGridLayout()
        grid_layout.addWidget(button_1,0,0)
        grid_layout.addWidget(button_2,0,1,1,2)
        grid_layout.addWidget(button_3,1,0,2,1)
        grid_layout.addWidget(button_4,1,1)
        grid_layout.addWidget(button_5,1,2)
        grid_layout.addWidget(button_6,2,1)
        grid_layout.addWidget(button_7,2,2)

        self.setLayout(grid_layout)