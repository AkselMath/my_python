import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/vkontakte_group_01_2016-08-01_2020-03-15.csv")
ae = df[df.Критерий == 'views']
ds = ae.Дата
dr = ae.Значение
dd = ds.iloc[0]
s = 0
a = []
for j in [16, 17, 18, 19]:
    for i in range(len(ae.index)):
        dd = ds.iloc[i]
        if eval(dd[8:]) > j:
            s += dr.iloc[i]
    a.append(s)
    s = 0
print(a)

ae = df[df.Критерий == 'visitors']
ds = ae.Дата
dr = ae.Значение
dd = ds.iloc[0]
s = 0
a = []
for j in [16, 17, 18, 19]:
    for i in range(len(ae.index)):
        dd = ds.iloc[i]
        if eval(dd[8:]) > j:
            s += dr.iloc[i]
    a.append(s)
    s = 0
print(a)


ae = df[df.Критерий == 'reach']
ds = ae.Дата
dr = ae.Значение
dd = ds.iloc[0]
s = 0
a = []
for j in [16, 17, 18, 19]:
    for i in range(len(ae.index)):
        dd = ds.iloc[i]
        if eval(dd[8:]) > j:
            s += dr.iloc[i]
    a.append(s)
    s = 0
print(a)

ae = df[df.Критерий == 'reach_subscribers']
ds = ae.Дата
dr = ae.Значение
dd = ds.iloc[0]
s = 0
a = []
for j in [16, 17, 18, 19]:
    for i in range(len(ae.index)):
        dd = ds.iloc[i]
        if eval(dd[8:]) > j:
            s += dr.iloc[i]
    a.append(s)
    s = 0
print(a)

ae = df[df.Критерий == 'age']
fr = df[df.Критерий == 'gender_age']
er = ae['Парам. №1'].value_counts()
re = fr['Парам. №2'].value_counts()
s = 0
a = []
for i in range(len(er.index)):
    a.append(re.iloc[i] + er.iloc[i])
print(a)

ae = df[(df.Критерий == 'gender') | (df.Критерий == 'gender_age')]
er = ae['Парам. №1'].value_counts(normalize=True)
print(er)

ae = df[df.Критерий == 'countries']['Парам. №1'].value_counts(normalize=True)
print(ae)