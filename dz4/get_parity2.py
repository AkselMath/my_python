#!/usr/bin/env python
# coding: utf-8

# In[1]:


def evenQ(a):
    '''
        >>> evenQ(2)
        'Чётное'
        >>> evenQ(3)
        'Нечётное'
    '''
    if a % 2 == 0:
        return "Чётное"
    else:
        return "Нечётное"

evenQ(3)

