import pandas as pd

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from functools import partial

from plotter import Plotter

buttons_names = [
    "overall_and_price_comp",
    "price_bar",
    "price_position_bar",
    "price_age_plot",
    "position_distribution",
    "most_valued_clubs"
]
number_of_plots = len(buttons_names)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "Fifa statistics"
        top = 200
        left = 200
        width = 800
        height = 700

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)

        self.canvas = None

        self.my_ui()
        self.set_buttons()

    def my_ui(self):
        self.canvas = Canvas(self)
        self.canvas.move(0, 0)

    def set_buttons(self):
        buttons = [None] * number_of_plots
        button_width = 150
        button_distances = 50
        for i in range(number_of_plots):
            buttons[i] = QPushButton(buttons_names[i], self)
            buttons[i].resize(button_width, 32)
            buttons[i].move(1210, 10 + button_distances * i)
            buttons[i].clicked.connect(partial(self.on_click, i))

    def on_click(self, number):
        self.canvas.update_plot(number)


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=12, height=8, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.update_plot(0)

    def update_plot(self, number):
        self.figure.clear()
        axes = self.figure.add_subplot(111)

        if number == 0:
            plotter_arg.overall_and_price_comp(axes)
        elif number == 1:
            plotter_arg.price_bar(axes)
        elif number == 2:
            plotter_arg.price_position_bar(axes)
        elif number == 3:
            plotter_arg.price_age_plot(axes)
        elif number == 4:
            plotter_arg.position_distribution(axes)
        elif number == 5:
            plotter_arg.most_valued_clubs(axes)

        self.figure.add_axes(axes)
        self.figure.tight_layout()
        self.draw()


with open('data.csv', 'r', encoding='utf-8') as csvFile:
    df = pd.read_csv('data.csv')

plotter_arg = Plotter(df)
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
