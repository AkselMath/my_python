#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system(' pip install PrettyTable')


# In[32]:


from prettytable import PrettyTable
h = ['1 месяц','2 месяц','3 месяц','4 месяц','5 месяц','6 месяц']
c = []
ves = int(input())

for i in range(6):
    ves = ves - 1.5
    c.append(ves)
    
table1 = PrettyTable(h)

table1.add_row(c[:6])

print(table1)


# In[ ]:




