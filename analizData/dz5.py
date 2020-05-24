import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/new_year_film.csv")

ranking = df['ranking']

p = 0
a = []
while p <= 149:
    a.append(float(str(ranking.iloc[p][0]) + '.' + str(ranking.iloc[p][2::])))
    p += 1
print(sum(a)/len(a))