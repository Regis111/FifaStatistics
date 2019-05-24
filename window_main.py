import sys

import pandas as pd
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction

from plotter import Plotter
from window_plots import WindowPlots
from window_search import WindowSearch


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        top = 100
        left = 100
        self.width = 1500
        self.height = 900
        self.button_width = 150
        self.button_height = 32
        self.button_distances = 50

        self.plotter = None

        with open('data.csv', 'r', encoding='utf-8') as csvFile:
            self.df = pd.read_csv('data.csv')

        self.setGeometry(top, left, self.width, self.height)
        self.setWindowIcon(QIcon('icon.ico'))
        self.setWindowTitle("Fifa Statistics")
        self.set_toolbar()

        self.start_window_plots()

    def set_toolbar(self):
        toolbar = self.addToolBar('Plots')

        show_plots_action = QAction('Plots', self)
        show_plots_action.triggered.connect(self.start_window_plots)

        search_action = QAction('Search', self)
        search_action.triggered.connect(self.start_window_search)

        toolbar.addAction(show_plots_action)
        toolbar.addAction(search_action)

    def start_window_plots(self):
        if not self.plotter:
            self.plotter = Plotter(self.df)

        window = WindowPlots(plotter_arg=self.plotter, parent=self)
        self.setWindowTitle("Plots")
        self.setCentralWidget(window)
        self.show()

    def start_window_search(self):
        window = WindowSearch(parent=self, df=self.df)
        self.setWindowTitle("Search")
        self.setCentralWidget(window)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
