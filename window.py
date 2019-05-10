import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from functools import partial
from plotter import Plotter
import types


plot_functions = [x for x in Plotter.__dict__.items() if isinstance(x[1], types.FunctionType) and x[0] != '__init__']
number_of_plots = len(plot_functions)


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
        print('xd')
        self.set_buttons()

    def my_ui(self):
        self.canvas = Canvas(self, plotter=Plotter(df))
        self.canvas.move(0, 0)

    def set_buttons(self):
        buttons = [None] * number_of_plots
        button_width = 150
        button_distances = 50
        for i in range(number_of_plots):
            buttons[i] = QPushButton(plot_functions[i][0], self)
            buttons[i].resize(button_width, 32)
            buttons[i].move(1210, 10 + button_distances * i)
            buttons[i].clicked.connect(partial(self.on_click, plot_functions[i][1]))

    def on_click(self, fun):
        self.canvas.update_plot(fun)


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=12, height=8, dpi=100, plotter=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.plotter = plotter

    def update_plot(self, fun):
        self.figure.clear()
        axes = self.figure.add_subplot(111)

        fun(self.plotter, ax=axes)

        self.figure.add_axes(axes)
        self.figure.tight_layout()
        self.draw()


with open('data.csv', 'r', encoding='utf-8') as csvFile:
    df = pd.read_csv('data.csv')


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
