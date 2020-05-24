import pandas as pd
import requests

df = pd.read_csv('https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/it_new.csv')
response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
currencies = response.json()

ds = {"zł": "PLN", "Kč": "CZK", "$": "USD", "€": "EUR"}
sa = ["zł", "Kč", "$", "€"]
zp = df["col"]
curs = df["curenc"]
a = []
# Определите среднюю з.п. по данным в рублях

for i in range(len(zp.index)):
    if curs.iloc[i] != '₽':
        a.append(zp.iloc[i]*currencies['Valute'][ds[curs.iloc[9]]]['Value'])
    else:
        a.append(zp.iloc[i])
print(a)

# Определите технологию с максимальной з.п. по данным в рублях
tex_col = df["Технология"].value_counts()
tex = df["Технология"]
b = []

for i in range(len(tex_col.index)):
    b.append([])
    for j in range(len(tex.index)):
        if tex_col.index[i] == tex.iloc[j]:
            b[-1].append(j)
k = 0
c = []
for i in range(len(b)):
    for j in range(len(b[i])):
        k += a[b[i][j]]
    c.append(k)
    k = 0
for i in range(len(c)):
    if c[i] == max(c):
        k = i
print(tex_col.index[k])
# Определите зарплаты работников, у которых в названии вакансии встречается слово Engineer
fd = []
dsd = df["Вакансия"]
for i in range(len(df.index)):
    if dsd.iloc[i].find('Engineer') != -1:
        fd.append(a[i])
print(fd)