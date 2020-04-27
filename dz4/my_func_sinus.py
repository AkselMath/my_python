#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
def cusf(a):
    if 0.2 <= a <= 0.9:
        return math.sin(a)
    else:
        return "1"

a = float(input())
cusf(a)

