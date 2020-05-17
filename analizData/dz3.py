import pandas as pd

url = 'https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv'

df = pd.read_csv(url)

# Задание 1

# grouped_df = (df.groupby(['Position'])['Value'].sum()/df.groupby(['Position'])['Wage'].sum()).sort_values(ascending=False)
# print(grouped_df.index[0])

# Задание 1

# koi = df.groupby(['Club'])['Wage'].agg(['mean','median'])
# k = 0
# for i in range(0, len(koi.index)):
#     if int(koi['mean'][i]) == int(koi['median'][i]):
#         k+=1
# print(k)

# Задание 2

# koi = df.groupby(['Club'])['Wage'].agg(['mean','median'])
# k = 0
# a = []
# for i in range(0, len(koi.index)):
#     if int(koi['mean'][i]) == int(koi['median'][i]):
#         k+=1
#         a.append(int(koi['mean'][i]))
#
# print(max(a))


# Задача 2
print(df[(df.Nationality == 'Argentina') & (df.Age == 20)].Wage.max())

# Задача 3
print(df[(df.Nationality == 'Argentina') & (df.Age == 30)].Wage.max())

# Задача 4
print(df[(df.Nationality == 'Argentina') & (df.Age == 30)].Wage.min())

