import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from functools import partial
from plotter import Plotter
import types

plot_functions = [x for x in Plotter.__dict__.items() if isinstance(x[1], types.FunctionType) and x[0] != '__init__']
number_of_plots = len(plot_functions)
top_number = 10


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "Fifa statistics"
        top = 100
        left = 100
        width = 1500
        height = 900
        self.button_width = 150
        self.button_distances = 50

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)

        self.canvas = None
        self.textbox_enter_top_number = None

        self.setWindowIcon(QIcon('icon.ico'))

        self.my_ui()
        self.set_functions_buttons()
        self.set_change_top_number_button()

    def my_ui(self):
        self.canvas = Canvas(self, plotter=Plotter(df))
        self.canvas.move(0, 0)

    def set_functions_buttons(self):
        buttons = [None] * number_of_plots
        for i in range(number_of_plots):
            buttons[i] = QPushButton(plot_functions[i][0], self)
            buttons[i].resize(self.button_width, 32)
            buttons[i].move(1210, 10 + self.button_distances * i)
            buttons[i].clicked.connect(partial(self.on_function_button_click, plot_functions[i][1]))

    def set_change_top_number_button(self):
        self.textbox_enter_top_number = QLineEdit(self)
        self.textbox_enter_top_number.resize(self.button_width, 32)
        self.textbox_enter_top_number.move(1210, 10 + self.button_distances * (number_of_plots + 1))

        button_change_top_number = QPushButton('Change top number', self)
        button_change_top_number.resize(self.button_width, 32)
        button_change_top_number.move(1210, 10 + self.button_distances * (number_of_plots + 2))
        button_change_top_number.clicked.connect(self.on_change_top_number_click)

    def on_function_button_click(self, fun):
        self.canvas.update_plot(fun)

    def on_change_top_number_click(self):
        global top_number
        entered_text = self.textbox_enter_top_number.text()
        try:
            new_number = int(entered_text)
            if new_number > 0:
                top_number = new_number
        except ValueError:
            QMessageBox.question(self, 'Error', 'Cannot parse argument: ' + entered_text, QMessageBox.Ok, QMessageBox.Ok)
        finally:
            self.textbox_enter_top_number.setText("")

        if self.canvas.fun:
            self.canvas.update_plot(self.canvas.fun)


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=12, height=8, dpi=100, plotter=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.plotter = plotter
        self.fun = None

    def update_plot(self, fun):
        self.figure.clear()
        axes = self.figure.add_subplot(111)
        self.fun = fun
        fun(self.plotter, ax=axes, top_number=top_number)

        self.figure.add_axes(axes)
        self.figure.tight_layout()
        self.draw()


with open('data.csv', 'r', encoding='utf-8') as csvFile:
    df = pd.read_csv('data.csv')

app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()
