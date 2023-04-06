from dialwidget import DialWidget
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton,QApplication,QToolTip
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, pyqtSignal

class DialWidgetUI(QWidget):

    switch_to_main_menu = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.title = 'dialWidget'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(250, 300)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        topLeftPoint = QApplication.desktop().availableGeometry().topLeft()
        self.move(topLeftPoint)

        layout = QVBoxLayout()

        backbtn = QPushButton("back", self)
        backbtn.setStyleSheet("background-color: rgba(222,184,135,255) ")
        backbtn.clicked.connect(self.switch_to_main_menu.emit)

        dialwidget = DialWidget()

        layout.addWidget(dialwidget)
        layout.addWidget(backbtn)

        self.setLayout(layout)