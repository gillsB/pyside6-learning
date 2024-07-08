from PySide6.QtWidgets import QWidget, QCheckBox, QRadioButton, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QCheckbox and QRadioButton")

        os = QGroupBox("Choose operating system")
        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggled)
        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggled)
        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_box_toggled)

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)


        ## exclusive checkboxes

        drinks = QGroupBox("choose a drink")
        beer = QCheckBox("Beer")
        juice = QCheckBox("Juice")
        coffee = QCheckBox("Coffee")
        beer.setChecked(True)


        exclusive_button_group = QButtonGroup(self)
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.addButton(coffee)
        exclusive_button_group.setExclusive(True)

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(juice)
        drink_layout.addWidget(coffee)
        drinks.setLayout(drink_layout)

        #radio buttons
        answers = QGroupBox("Choose answer")
        answer_a = QRadioButton("A")
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")

        answers_layout = QVBoxLayout()
        answers_layout.addWidget(answer_a)
        answers_layout.addWidget(answer_b)
        answers_layout.addWidget(answer_c)
        answers.setLayout(answers_layout)


        layout = QHBoxLayout()
        layout.addWidget(os)
        layout.addWidget(drinks)

        layout_v = QVBoxLayout()
        layout_v.addLayout(layout)
        layout_v.addWidget(answers)

        self.setLayout(layout_v)






    def windows_box_toggled(self,checked):
        if(checked):
            print("windows box checked")
        else:
            print("windows box unchecked")
    def linux_box_toggled(self,checked):
        if(checked):
            print("linux box checked")
        else:
            print("linux box unchecked")
    def mac_box_toggled(self, checked):
        if(checked):
            print("mac box checked")
        else:
            print("mac box unchecked")