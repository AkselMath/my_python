#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random

def jd(a):
    p = random.randint(1,4)
    if a == p:
        return "Вы угадали"
    elif a < p:
        return "Мало"
    else:
        return "Много"

a = int(input())
jd(a)


# In[ ]:




