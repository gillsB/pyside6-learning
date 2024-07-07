from PySide6.QtWidgets import QWidget, QTextEdit, QHBoxLayout, QVBoxLayout, QPushButton


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTextEdit")

        self.text_edit = QTextEdit()

        text_to_console = QPushButton("Current Text to console")
        text_to_console.clicked.connect(self.text_to_console)

        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy)

        cut_botton = QPushButton("Cut")
        cut_botton.clicked.connect(self.text_edit.cut)

        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.paste)

        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.text_edit.redo)

        set_plain_button = QPushButton("Set plain text")
        set_plain_button.clicked.connect(self.set_plain_text)

        set_html_button = QPushButton("Set html")
        set_html_button.clicked.connect(self.set_html)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear)


        h_layout = QHBoxLayout()
        h_layout.addWidget(text_to_console)
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_botton)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_plain_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(clear_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)

    def set_plain_text(self):
        self.text_edit.setPlainText("Hello")

    #write something in html i.e. <h1> Hello this is a header</h1> then click the button
    def set_html(self):
        self.text_edit.setHtml(self.text_edit.toPlainText())

    def text_to_console(self):
        print(self.text_edit.toPlainText())

    #this just shows that you can "override" a base function to do something else 
    # (not really an override more just that you can call it from a function and not just from the connect)
    def paste(self):
        self.text_edit.paste()