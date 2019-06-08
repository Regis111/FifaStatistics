
import pandas as pd
import matplotlib.pyplot as plt

from plotter import Plotter

from urllib.request import urlopen, Request

with open('data.csv', 'r', encoding='utf-8') as csvFile:
    df = pd.read_csv('data.csv')

list = ['Name', 'Age', 'Nationality', 'Overall', 'Club', 'Value',
                   'Wage', 'Skill Moves', 'Position', 'Height', 'Weight']

for el in list:
    print(el, type(df.loc[[0], [el]]), df.loc[[0], [el]])


plotter = Plotter(df)
# print plots
plotter.overall_and_price_comp()
plt.show()
plotter.price_bar()
plt.show()
plotter.price_position_bar()
plt.show()
plotter.price_age_plot()
plt.show()
plotter.age_distribution()
plt.show()
plotter.position_distribution()
plt.show()
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