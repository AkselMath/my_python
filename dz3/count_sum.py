#!/usr/bin/env python
# coding: utf-8

# In[17]:


a = input()
k = 0
for i in a:
    if int(i) % 2 == 1:
        k = k + int(i)**2
print(k)

