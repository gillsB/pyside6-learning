from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel and QLineEdit")

        label = QLabel("Name : ")
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.text_changed)
        self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)

        #these two basically do the same thing, both trigger upon hitting return/enter
        #self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.returnPressed.connect(self.return_pressed)

        self.line_edit.selectionChanged.connect(self.selection_changed)

        self.line_edit.textEdited.connect(self.text_edited)



        button = QPushButton("check")
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel("QLabel")
        

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)

    def button_clicked(self):
        self.text_holder_label.setText(self.line_edit.text())

    def text_changed(self):
        self.text_holder_label.setText(self.line_edit.text())

    def cursor_position_changed(self, old, new):
        print("old position: ",old," New position: ",new)


    def editing_finished(self):
        print("editing finished")
    def return_pressed(self):
        print("return pressed")

    def selection_changed(self):
        print("selection changed :",self.line_edit.selectedText())

    def text_edited(self, new_text):
        print("text edited, new text: ", new_text)