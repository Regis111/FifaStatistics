import pandas as pd

from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, \
    QFileDialog, QComboBox
from PyQt5.QtWidgets import QApplication, QTableView

from pandas_model import PandasModel
import copy


class WindowSearch(QWidget):
    def __init__(self, parent, df):
        QWidget.__init__(self, parent=None)

        self.df = copy.copy(self.prepare_df(df))

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        self.search_textbox = QLineEdit(self)
        self.search_textbox.setPlaceholderText("Enter searched name")
        h_layout.addWidget(self.search_textbox)

        self.combo_box = QComboBox()
        self.combo_box.addItems(self.df.columns)
        h_layout.addWidget(self.combo_box)

        self.search_button = QPushButton("Search", self)
        h_layout.addWidget(self.search_button)

        v_layout.addLayout(h_layout)

        self.table = QTableView(self)
        v_layout.addWidget(self.table)

        self.setLayout(v_layout)

        self.model = PandasModel(self.df)
        self.table.setModel(self.model)

        self.search_button.clicked.connect(self.search_clicked)
        self.table.setSortingEnabled(True)

    def search_clicked(self):
        entered_text = self.search_textbox.text()
        entered_category = self.combo_box.currentText()
        if entered_category in ['Name', 'Nationality', 'Club', 'Position', 'Height', 'Weight']:
            result = self.df[self.df[entered_category].str.contains(entered_text, na=False)]
        else:
            result = self.df[self.df[entered_category] == float(entered_text)]

        self.model.update(result)

    @staticmethod
    def prepare_df(df):
        columns = ['Name', 'Age', 'Nationality', 'Overall', 'Club', 'Value',
                   'Wage', 'Skill Moves', 'Position', 'Height', 'Weight']

        return df[columns]
