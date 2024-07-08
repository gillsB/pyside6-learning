from PySide6.QtWidgets import QWidget, QTabWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QSpacerItem, QHBoxLayout


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTabWidget")

        tab_widget = QTabWidget(self)

        widget_form = QWidget()
        label_full_name = QLabel("Full Name: ")
        line_edit_full_name = QLineEdit()
        form_layout = QHBoxLayout()
        form_layout.addWidget(label_full_name)
        form_layout.addWidget(line_edit_full_name)
        widget_form.setLayout(form_layout)


        widget_buttons = QWidget()
        button_1 = QPushButton("One")
        button_1.clicked.connect(self.button_1_clicked)
        button_2 = QPushButton("Two")
        button_2.clicked.connect(self.button_2_clicked)
        button_3 = QPushButton("Three")
        button_3.clicked.connect(self.button_3_clicked)

        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(button_1)
        buttons_layout.addWidget(button_2)
        buttons_layout.addWidget(button_3)
        widget_buttons.setLayout(buttons_layout)

        tab_widget.addTab(widget_form, "Information")
        tab_widget.addTab(widget_buttons, "Buttons")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)




    def button_1_clicked(self):
        print("button1 clicked")
    def button_2_clicked(self):
        print("button2 clicked")
    def button_3_clicked(self):
        print("button3 clicked")