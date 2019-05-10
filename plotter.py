import pandas as pd


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
    def overall_and_price_comp(self, ax):
        self.df.loc[:, ['Overall', 'ValueReal']].plot(kind='scatter', x='Overall', y='ValueReal', ax=ax)

    # ceny slupkowo
    def price_bar(self, ax):
        self.df['ValueIntervals'].value_counts().sort_index().plot(kind='bar', ax=ax)

    # cena a pozycja
    def price_position_bar(self, ax):
        self.df.loc[:, ['ValueReal', 'Position']].groupby('Position').mean().plot(kind='bar', ax=ax)

    # cena a wiek
    def price_age_plot(self, ax):
        self.df.loc[:, ['ValueReal', 'AgeIntervals']].groupby('AgeIntervals').mean().plot(kind='bar', ax=ax)

    # kluby najbardziej wartościowe
    def most_valued_clubs(self, ax):
        self.df.loc[:, ['ValueReal', 'Club']].groupby('Club').sum().sort_values('ValueReal').tail(10).plot(kind='barh', ax=ax)

    # kluby z najlepszymy zarobkami

    # rozkład całego zbioru : wiek, pozycja, kraj, zarobki
    def age_distribution(self, ax):
        self.df['AgeIntervals'].value_counts().sort_index().plot(kind='bar', ax=ax)

    def position_distribution(self, ax):
        self.df['Position'].value_counts().sort_index().plot(kind='bar', ax=ax)

    # kraje z najlepszymi piłkarzami
