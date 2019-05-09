import pandas as pd
import matplotlib.pyplot as plt


def value_of_price(value):
    length = len(value)
    if length == 2:
        return 0
    letter = value[length - 1]
    value = value[1:length - 1]
    value = float(value)
    if letter == 'M':
        value = value * 1000000
    else:
        value = value * 1000
    return value


class Plotter:
    def __init__(self, df):
        self.df = df
        # prepare data
        intervals = [i * 10000000 for i in range(10)]
        intervals.append(float("inf"))
        df['ValueReal'] = df.apply(lambda row: value_of_price(row.Value), axis=1)
        df['ValueIntervals'] = pd.cut(df.ValueReal, intervals, include_lowest=True)
        df['WageReal'] = df.apply(lambda row: value_of_price(row.Wage), axis=1)
        intervals = [i for i in range(15, 48, 3)]
        df['AgeIntervals'] = pd.cut(df.Age, intervals)

    # dwie funkcje od wykresu ceny od overalla

    def overall_and_price_comp(self):
        overalls = self.df.loc[:, 'Overall']
        prices = self.df.loc[:, 'ValueReal']
        return plt.scatter(overalls, prices)

    # ceny slupkowo
    def price_bar(self):
        a = self.df['ValueIntervals'].value_counts().sort_index()
        return a.plot.bar()

    # cena a pozycja
    def price_position_bar(self):
        a = self.df.loc[:, ['ValueReal', 'Position']].groupby('Position').mean()
        return a.plot.bar()

    # cena a wiek
    def price_age_plot(self):
        a = self.df.loc[:, ['ValueReal', 'AgeIntervals']].groupby('AgeIntervals').mean()
        return a.plot.bar()

    # kluby najbardziej wartościowe
    def most_valued_clubs(self):
        a = self.df.loc[:, ['ValueReal', 'Club']].groupby('Club').sum().sort_values('ValueReal').tail(10)
        return a.plot.barh()

    # kluby z najlepszymy zarobkami

    # rozkład całego zbioru : wiek, pozycja, kraj, zarobki
    def age_distribution(self):
        a = self.df['AgeIntervals'].value_counts().sort_index()
        return a.plot.bar()

    def position_distribution(self):
        a = self.df['Position'].value_counts().sort_index()
        return a.plot.bar()

    # kraje z najlepszymi piłkarzami
