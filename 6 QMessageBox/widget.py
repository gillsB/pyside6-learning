from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox")

        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical = QPushButton("critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton("question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton("information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("about")
        button_about.clicked.connect(self.button_clicked_about)

        layout = QVBoxLayout()
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)
        self.setLayout(layout)




    def button_clicked_hard(self):

        #example of long way
        message = QMessageBox()
        message.setMinimumSize(700,200)
        message.setWindowTitle("Message Title")
        message.setText("Something Happened")
        message.setInformativeText("Do you want to do something?")
        message.setIcon(QMessageBox.Warning)
        message.setStandardButtons(QMessageBox.Ok |QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("user chose OK")
        else:
            print("user chose Cancel")

    def button_clicked_critical(self):
        ret = QMessageBox.critical(self,"Critical Message", "Critical", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("user chose OK")
        else:
            print("user chose Cancel")
    def button_clicked_question(self):
        ret = QMessageBox.question(self,"question Message", "question", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("user chose OK")
        else:
            print("user chose Cancel")
    def button_clicked_information(self):
        ret = QMessageBox.information(self,"information Message", "information", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("user chose OK")
        else:
            print("user chose Cancel")
    def button_clicked_warning(self):
        ret = QMessageBox.warning(self,"warning Message", "warning", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("user chose OK")
        else:
            print("user chose Cancel")
    def button_clicked_about(self):
        ret = QMessageBox.about(self,"about Message", "about")
        if ret == QMessageBox.Ok:
            print("user chose OK")
        else:
            print("About only has OK")