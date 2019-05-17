import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

from window_plots import WindowPlots
from window_search import WindowSearch


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        top = 100
        left = 100
        width = 1500
        height = 900
        self.button_width = 150
        self.button_height = 32
        self.button_distances = 50
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon('icon.ico'))
        self.setWindowTitle("Fifa Statistics")
        self.button_plots = None
        self.button_search = None
        self.set_buttons()

    def set_buttons(self):
        self.button_plots = QPushButton("Show plots", self)
        self.button_plots.resize(self.button_width, self.button_height)
        self.button_plots.move(100, 100)
        self.button_plots.clicked.connect(self.start_window_plots)

        self.button_search = QPushButton("Search", self)
        self.button_search.resize(self.button_width, self.button_height)
        self.button_search.move(100, 100 + self.button_distances)
        self.button_search.clicked.connect(self.start_window_search)

    def start_window_plots(self):
        self.hide_buttons()
        window = WindowPlots(self)
        self.setWindowTitle("Plots")
        self.setCentralWidget(window)
        self.show()

    def start_window_search(self):
        self.hide_buttons()
        window = WindowSearch(self)
        self.setWindowTitle("Search")
        self.setCentralWidget(window)
        self.show()

    def hide_buttons(self):
        self.button_search.hide()
        self.button_plots.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
