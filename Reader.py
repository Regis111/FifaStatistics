import pandas as pd
import matplotlib.pyplot as plt

'import numpy as np'
from PIL import Image
from urllib.request import urlopen, Request


# dwie funkcje od wykresu ceny od overalla
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


def overall_and_price_comp(df):
    overalls = df.loc[:, 'Overall']
    prices = df.loc[:, 'ValueReal']
    plt.scatter(overalls, prices)
    plt.show()


# ceny slupkowo
def price_bar(df):
    a = df['ValueIntervals'].value_counts().sort_index()
    a.plot.bar()
    plt.show()


# cena a pozycja
def price_position_bar(df):
    a = df.loc[:,['ValueReal', 'Position']].groupby('Position').mean()
    a.plot.bar()
    plt.show()


# cena a wiek
def price_age_plot(df):
    a = df.loc[:,['ValueReal', 'AgeIntervals']].groupby('AgeIntervals').mean()
    a.plot.bar()
    plt.show()


# kluby najbardziej wartościowe
def most_valued_clubs(df):
    a = df.loc[:, ['ValueReal', 'Club']].groupby('Club').sum().sort_values('ValueReal').tail(10)
    a.plot.barh()
    plt.show()

# kluby z najlepszymy zarobkami

# rozkład całego zbioru : wiek, pozycja, kraj, zarobki
def age_distribution(df):
    a = df['AgeIntervals'].value_counts().sort_index()
    a.plot.bar()
    plt.show()

def position_distribution(df):
    a = df['Position'].value_counts().sort_index()
    a.plot.bar()
    plt.show()

def age_distribution(df):
    a = df['AgeIntervals'].value_counts().sort_index()
    a.plot.bar()
    plt.show()

# kraje z najlepszymi piłkarzami


with open('data.csv', 'r', encoding='utf-8') as csvFile:
    df1 = pd.read_csv('data.csv')
    df = df1  # .tail(600)

# prepare data
intervals = [i * 10000000 for i in range(10)]
intervals.append(float("inf"))
df['ValueReal'] = df.apply(lambda row: value_of_price(row.Value), axis=1)
df['ValueIntervals'] = pd.cut(df.ValueReal, intervals, include_lowest=True)
df['WageReal'] = df.apply(lambda row: value_of_price(row.Wage), axis=1)
#
intervals = [i for i in range(15,48,3)]
df['AgeIntervals'] = pd.cut(df.Age, intervals)


# print plots
#overall_and_price_comp(df.head(50))
#price_bar(df.head(50))
#price_position_bar(df.head(50))
#price_age_plot(df)
#most_valued_clubs(df)
#age_distribution(df)
#wage_distribution(df)
#position_distribution(df)


# do zdjec
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 '
                         'Safari/537.3'}
urls = df.head(10)
for index, row in urls.iterrows():
    url = row['Photo']
    name = row['Name']
    try:
        req = Request(url=url, headers=headers)
        im = Image.open(urlopen(req))
        # im.show()
    except:
        print(url, name)