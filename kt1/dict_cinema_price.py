#!/usr/bin/env python
# coding: utf-8

# In[53]:


from pprint import pprint
s = {
    'Паразиты': {'Сеансы': {12: 250, 16: 350, 20: 450 } },
    '1917': {'Сеансы': {10: 250, 13: 350, 16: 450 } },
    'Соник в кино': {'Сеансы': {10: 350, 14: 450, 18: 450 } }
} 
print(s)
print('Программа для подсчета стоимости билетов в кино.')

h = input("Выбрать фильм: ")
g = input("Выбрать день (сегодня, завтра): ")
c = int(input("Выбрать время: "))
v = int(input("Выбрать количество билетов: "))
print('Выбрали фильм:', h, 'День:', g, 'Время:', c, 'Количество билетов:',v)
if g == 'сегодня' and v >= 20:
    print('Результат:', 0.75 * s[h]['Сеансы'][c] * v, 'руб')
else:
    if g == 'сегодня':
        print('Результат:', 0.95 * s[h]['Сеансы'][c] * v, 'руб')
    if v >= 20:
            print('Результат:', 0.80 * s[h]['Сеансы'][c] * v, 'руб')
