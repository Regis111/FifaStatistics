import pandas as pd
import matplotlib.pyplot as plt
'import numpy as np'

# dwie funkcje od wykresu ceny od overalla
def value_of_price(value):
    length = len(value)
    if length == 2:
        return 0
    letter = value[length-1]
    value = value[1:length-1]
    value = float(value)
    if letter == 'M':
        value = value * 1000000
    else:
        value = value * 1000
    return value


def overall_and_price_comp(df):
    overalls = df.loc[:, 'Overall']
    prices = df.loc[:, 'Value']
    prices = list(map(value_of_price, prices))
    plt.plot(overalls, prices)
    plt.show()

# cena a pozycja

# cena a wiek

# kluby najbardziej wartościowe

# rozkład całego zbioru : wiek, pozycja, kraj, zarobki

# kluby z najlepszymy zarobkami

# kraj z najlepszymi piłkarzami


with open('data.csv', 'r', encoding='utf-8') as csvFile:
    df1 = pd.read_csv('data.csv')
    df = df1.head(600)
    overall_and_price_comp(df)
