
import pandas as pd
import matplotlib.pyplot as plt

from plotter import Plotter

'import numpy as np'
from PIL import Image

from urllib.request import urlopen, Request

with open('data.csv', 'r', encoding='utf-8') as csvFile:
    df = pd.read_csv('data.csv')

# print plots
# overall_and_price_comp(df.head(50))
# price_bar(df.head(50))
# price_position_bar(df.head(50))
# price_age_plot(df)
# most_valued_clubs(df)
# age_distribution(df)
# wage_distribution(df)
# position_distribution(df)

plotter = Plotter(df)
plotter.most_valued_clubs()
plt.show()


# do zdjec
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 '
                         'Safari/537.3'}
urls = df.head(10)
for index, row in urls.iterrows():
    url = row['Photo']
    name = row['Name']
    try:
        req = Request(url=url, headers=headers)
        # im = Image.open(urlopen(req))
        # im.show()
    except:
        print(url, name)