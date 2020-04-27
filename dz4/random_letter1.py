#!/usr/bin/env python
# coding: utf-8

# In[28]:


import random
a = ["абрикос", "dark souls", "bloodborne"]
r = random.randint(0,len(a)-1)
g = random.randint(0,len(a[r])-1)
print(a[r][0:g] + "?" + a[r][(g + 1)::])
s = input("Введите букву:")
if a[r][g] == s:
    print("Победа")
else:
    print("Не победа")

