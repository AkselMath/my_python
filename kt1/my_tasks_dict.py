#!/usr/bin/env python
# coding: utf-8

# In[22]:


from pprint import pprint
a = [{}]
f = 1
while f != 3:
    print("Простой todo:\n1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.")
    f = int(input())
    if f == 1:
        
        h = input("Сформулируйте задачу: ")
        g = input("Добавьте категорию к задаче: ")
        c = input("Добавьте время к задаче: ")
        a[len(a)-1].update({'Задача': h, 'Категория': g, 'Дата': c})

    if f == 2:
        pprint(a)


# In[ ]:




