from PyQt5.QtWidgets import QWidget, QPushButton


class WindowSearch(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        QPushButton("text2", self)
