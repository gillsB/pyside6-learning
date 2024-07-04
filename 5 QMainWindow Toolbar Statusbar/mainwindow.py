from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon

class Window(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Window")

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_action)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        edit_menu = menu_bar.addMenu("Window")
        edit_menu = menu_bar.addMenu("Setting")
        edit_menu = menu_bar.addMenu("Help")

        toolbar = QToolBar("Main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

        action1 = QAction("Action", self)
        action1.setStatusTip("Status Tip for action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("start.png"), "Some other action", self)
        action2.setStatusTip("Status Tip for action2")
        action2.triggered.connect(self.toolbar_button_click)
        action2.setCheckable(True)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("click here"))

        self.setStatusBar(QStatusBar(self))

        button1 = QPushButton("Button")
        button1.clicked.connect(self.button_clicked)
        self.setCentralWidget(button1)


    def quit_action(self):
        self.app.quit()

    def toolbar_button_click(self):
        self.statusBar().showMessage("Message", 3000)

    def button_clicked(self):
        print("clicked")