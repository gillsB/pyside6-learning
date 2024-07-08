from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy, QLineEdit, QPushButton


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size policies and stretches")


        label = QLabel("Text input: ")
        line_edit = QLineEdit()

        #default
        #line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        #no scaling
        line_edit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)

        button_1 = QPushButton("one")
        button_2 = QPushButton("two")
        button_3 = QPushButton("three")


        #layout 2nd argument describes how much space it will gain as the window gets larger.
        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(button_1, 2)
        h_layout_2.addWidget(button_2, 1)
        h_layout_2.addWidget(button_3, 1)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)

        self.setLayout(v_layout)