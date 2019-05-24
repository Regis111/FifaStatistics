import pandas as pd

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, \
    QFileDialog
from PyQt5.QtWidgets import QApplication, QTableView

from pandas_model import PandasModel


class WindowSearch(QWidget):
    def __init__(self, parent, df):
        QWidget.__init__(self, parent=None)

        self.df = df

        v_layout = QVBoxLayout(self)
        h_layout = QHBoxLayout()

        self.search_textbox = QLineEdit(self)
        self.search_textbox.setPlaceholderText("Enter searched name")
        h_layout.addWidget(self.search_textbox)

        self.search_button = QPushButton("Search", self)
        h_layout.addWidget(self.search_button)

        v_layout.addLayout(h_layout)
        self.table = QTableView(self)

        v_layout.addWidget(self.table)

        self.model = PandasModel(self.df)
        self.table.setModel(self.model)

        self.search_button.clicked.connect(self.search_clicked)
        self.table.setSortingEnabled(True)

    def search_clicked(self):
        entered_text = self.search_textbox.text()
        print(entered_text)
        result = self.df.query('Name.str.contains("{0}")'.format(entered_text))
        self.model.update(result)
