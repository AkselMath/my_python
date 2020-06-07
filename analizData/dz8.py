import pandas as pd
import pymorphy2
import json

# Определите распределение зарплат в компании Тинькофф по сведениям сайта hh
tinkof = []
with open('data.json', encoding='UTF8') as f:
    d = f.readlines()

for k in d:
    tinkof.append(json.loads(k))

tinkofDataFrame = pd.DataFrame(tinkof[1::2])

print(tinkofDataFrame.groupby(['income'])['vacancy'].value_counts())

# Определите статистику встречаемости отдельных слов в поисковых фразах.
# Это позволит понять тематику данного сайта и настроить показ рекламы.
url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stat/yandex-stat-q.csv"
df = pd.read_csv(url)
morph = pymorphy2.MorphAnalyzer()

searchPhrase = df['Поисковая фраза']
visits = df['Визиты']

a = []
b = []
for j in range(len(searchPhrase.index)):
    for i in searchPhrase.iloc[j].split():
        a.append(morph.parse(i.lower())[0].normal_form)

    b.append([visits.iloc[j]]*len(searchPhrase.iloc[j].split()))

b = [item for sublist in b for item in sublist]


data = {"Слова": pd.Series(a), "Визиты": pd.Series(b)}
data1 = pd.DataFrame(data)

print(data1.groupby(['Слова'])['Визиты'].sum())
