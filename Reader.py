import pandas as pd

with open('data.csv','r',encoding='utf-8') as csvFile:
    df=pd.read_csv('data.csv')
    