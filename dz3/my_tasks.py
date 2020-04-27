#!/usr/bin/env python
# coding: utf-8

# In[30]:


a = []
f = 1
while f != 3:
    print("Простой todo:\n1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.")
    f = int(input())
    if f == 1:
        a.append([""])
        
        h = input("Сформулируйте задачу: ")
        g = input("Добавьте категорию к задаче: ")
        c = input("Добавьте время к задаче: ")
        a[len(a)-1] = a[len(a)-1][0]+ "Задача: " + h + " Категория: " + g + " Дата: " + c

    if f == 2:
        for i in a:
            print(i)


# In[ ]:




