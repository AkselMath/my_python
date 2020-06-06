import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/vkontakte_group_01_2016-08-01_2020-03-15.csv")

# определить статистику посещаемости группы просмотры в год views
criterionViews = data[data.Критерий == 'views']
dateViews = criterionViews.Дата
valueViews = criterionViews.Значение
dd = dateViews.iloc[0]
s = 0
viewsPerYear = []
year = [19, 18, 17, 16, 15]
j = 0
for i in range(len(criterionViews.index)-1):
    if eval(dd[8:]) > year[j]:
        s += valueViews.iloc[i]
        dd = dateViews.iloc[i + 1]
    else:
        j += 1
        dd = dateViews.iloc[i + 1]
        viewsPerYear.append(s)
        s = valueViews.iloc[i]
viewsPerYear.append(s)
print("статистика посещаемости группы просмотры в год")
print({"2020 год": viewsPerYear[0], "2019 год": viewsPerYear[1], "2018 год": viewsPerYear[2],
       "2017 год": viewsPerYear[3], "2016 год": viewsPerYear[4]})

# определить статистику посещаемости группы посещения в год visitors
criterionVisitors = data[data.Критерий == 'visitors']
dateVisitors = criterionVisitors.Дата
valueVisitors = criterionVisitors.Значение
ee = dateVisitors.iloc[0]
visitsPerYear = []
year = [19, 18, 17, 16, 15]
j = 0
s = 0
for i in range(len(criterionVisitors.index) - 1):
    if eval(ee[8:]) > year[j]:
        s += valueVisitors.iloc[i]
        ee = dateVisitors.iloc[i + 1]
    else:
        j += 1
        ee = dateVisitors.iloc[i + 1]
        visitsPerYear.append(s)
        s = valueVisitors.iloc[i]

visitsPerYear.append(s)
print("статистика посещаемости группы посещения в год")
print({"2020 год": visitsPerYear[0], "2019 год": visitsPerYear[1], "2018 год": visitsPerYear[2],
       "2017 год": visitsPerYear[3], "2016 год": visitsPerYear[4]})


# статистика охвата аудитории по годам reach
criterionReach = data[data.Критерий == 'reach']
dateReach = criterionReach.Дата
valueReach = criterionReach.Значение
kk = dateReach.iloc[0]
reachPerYear = []
year = [19, 18, 17, 16, 15]
j = 0
s = 0
for i in range(len(criterionReach.index) - 1):
    if eval(kk[8:]) > year[j]:
        s += valueReach.iloc[i]
        kk = dateReach.iloc[i + 1]
    else:
        j += 1
        kk = dateReach.iloc[i + 1]
        reachPerYear.append(s)
        s = valueReach.iloc[i]
reachPerYear.append(s)
print(reachPerYear)
print("статистика охвата аудитории по годам")
print({"2020 год": reachPerYear[0], "2019 год": reachPerYear[1], "2018 год": reachPerYear[2],
       "2017 год": reachPerYear[3], "2016 год": reachPerYear[4]})


# статистика прироста подписчиков по годам reach_subscribers
criterionReachSubscribers = data[data.Критерий == 'reach_subscribers']
dateReachSubscribers = criterionReachSubscribers.Дата
valueReachSubscribers = criterionReachSubscribers.Значение
mm = dateReachSubscribers.iloc[0]
reachSubscribersPerYear = []
year = [19, 18, 17, 16, 15]
j = 0
s = 0
for i in range(len(criterionReachSubscribers.index) - 1):
    if eval(mm[8:]) > year[j]:
        s += valueReachSubscribers.iloc[i]
        mm = dateReachSubscribers.iloc[i + 1]
    else:
        j += 1
        mm = dateReachSubscribers.iloc[i + 1]
        reachSubscribersPerYear.append(s)
        s = valueReachSubscribers.iloc[i]
reachSubscribersPerYear.append(s)
print(reachSubscribersPerYear)
print("статистика количества подписциков по годам")
print({"2020 год": reachSubscribersPerYear[0], "2019 год": reachSubscribersPerYear[1], "2018 год": reachSubscribersPerYear[2],
       "2017 год": reachSubscribersPerYear[3], "2016 год": reachSubscribersPerYear[4]})


# анализ демографии age
print(data.loc[data.Критерий == "age"].groupby(["Парам. №1"])["Значение"].sum())

# анализ демографии gender, gender_age
criterionGender_GenderAge = data[(data.Критерий == 'gender') | (data.Критерий == 'gender_age')]
er = criterionGender_GenderAge['Парам. №1'].value_counts(normalize=True)
print(er)

# анализ демографии countries
criterionCountries = data[data.Критерий == 'countries']['Парам. №1'].value_counts(normalize=True)
print(criterionCountries)

# провести анализ обратной связи
# Группу просматривают стобильно около 7000 людей ежегодно. Год 2020 только начаался и поэтому количество просмотров мало
# Посещают группу стабильно 5000 каждый год, однако за 2017 год наблюдается скачёк как по просмотрам так и по посощаемости
# Общий охват паблика ежегодно больше 10000, что несомненно хорошо
# Количество подписчиков увеличевается каждый год более чем на 2000.
# Сначала их было 3494, потом они увеличелись на 4487 и т. д.
# Возраст участников группы равномерен, за исключениев возростного промежутка 1-18, этих людей меньшенство.
# Больше всего людей в возрасте 18-21
# Женщин и мужчин примерно одинаково
# Большая часть людей из постсоветского пространства



# обосновать, подходит ли данная группа для продвижения нового товара среди активных пользователей из России моложе 30 лет?
# На мой взгляд подходит, так как группа развивается, колличество людей из России наибольшее число и так же
# людей младше 30 крайне много в этой группе
