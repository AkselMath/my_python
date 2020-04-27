#!/usr/bin/env python
# coding: utf-8

# In[2]:


k = 0
a = input()
while a != "STOP":
    if a.isdigit():
        k = k + int(a)
    a = input()
print(k)

