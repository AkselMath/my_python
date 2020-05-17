import pandas as pd

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv"

football = pd.read_csv(url)


# Сколько футбольных клубов представлено в датасете?
# s = football['Club'].value_counts()
# print(len(s.index))

# Как называется футбольный клуб, представленный наименьшим количеством игроков в датасете?
# s = football['Club'].value_counts()
# print(s.index[-1])

# s = football['Position'].value_counts(normalize=True)
# print(s.loc[s > 0.1])
# print(s.loc[s < 0.01])

# В каких пределах находятся худшие 20% показателей точности ударов ногой?
# s = football['FKAccuracy'].value_counts(bins=5)
# print(s.index[3].left, s.index[3].right)

#Задача 1
# s = football[football.Nationality == 'Spain']["Wage"].value_counts(bins=4)
# for i in range(len(s.index)):
#     if s.index[i].left <= s.index[0].left:
#         f = i
# print(s.iloc[f])
# Задача 2

# print(football[football.Club == "Manchester United"]['Nationality'].nunique())

# Задача 3

# print(football[(football.Nationality == 'Brazil') & (football.Club == 'Juventus')])

# Задача 4

# print(football[football.Age > 35]["Club"].value_counts().index[0])

# Задача 5

# s = football[football.Nationality == "Argentina"]["Age"].value_counts(bins=4)
#
# for i in range(len(s.index)):
#     if s.index[i].left <= 35.75 and s.index[i].right >= 41:
#         f = i
# print(s.iloc[f])

# Задача 6
# s = football[football.Nationality == 'Spain']["Age"].value_counts(normalize=True)
# for i in range(len(s.index)):
#     if s.index[i] == 21:
#         f = i
# print(round(s.iloc[f]*100, 2))
