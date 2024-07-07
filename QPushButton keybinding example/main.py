import sys
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class Button(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.listening = False
        self.clicked.connect(self.enable_listening)
        self.installEventFilter(self)

    def enable_listening(self):
        self.listening = True
        self.setText("Press a key")

    def keyPressEvent(self, event):
        # <= 16000000 or else you get something like Ctrl + Control (upon just using pressing ctrl, auto completes and cant even set a normal key) for all modifiers 
        if self.listening and event.key() <= 16000000:
            self.listening = False
            key = event.key()
            modifiers = event.modifiers()

            key_name = QKeySequence(key).toString()
            modifier_names = []

            if modifiers & Qt.ShiftModifier:
                modifier_names.append("Shift")
            if modifiers & Qt.ControlModifier:
                modifier_names.append("Ctrl")
            if modifiers & Qt.AltModifier:
                modifier_names.append("Alt")
            #meta key is pretty much irrelevant in modern day, but added because example I found supported it
            if modifiers & Qt.MetaModifier:
                modifier_names.append("Meta")
            #super is equivalent to Windows key/Mac command key. But windows kind of lacks support for it as windows key by default is bound to
            #bring up the start menu. So also kind of irrelevant
            if modifiers & Qt.SuperModifier:
                modifier_names.append("Super")

            full_key_name = " + ".join(modifier_names + [key_name])
            self.setText(full_key_name)
        else:
            super().keyPressEvent(event)

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress and self.listening:
            self.keyPressEvent(event)
            return True
        return super().eventFilter(source, event)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.button = Button("Click to change keybind")
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.setWindowTitle("QPushButton keybind")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())