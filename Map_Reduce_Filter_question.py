#!/usr/bin/env python
# coding: utf-8

# In[14]:


# Write a Python program to triple all numbers of a given list of integers. Use Python map
def triple(a):
    d=a+a+a
    return(d)
x = map(triple, (1,2,4))
print(list(x))


# In[16]:


# Write a Python program to add three given lists using Python map and lambda
result = map((lambda x,y,z: x + y + z) ,[1,2],[2,3],[3,4])
print(list(result))


# In[4]:


# Write a Python program to add two given lists and find the difference between lists

"""
sample list
nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]
output  - [(6, 6), (6, 4), (10, -4), (16, 2)]

"""
result = map((lambda x,y: ((x+y),(x-y))) ,[6, 5, 3, 9],[0, 1, 7, 7])
print(list(result))


# In[16]:


# Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters from a given sequence
def change_cases(s):
    return str(s).upper(), str(s).lower()
chrars = ['a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a']
d=set(chrars)
print(d)
result = map(change_cases, d)
print(list(result))


# In[24]:


# Filter out the fruits that start with A 
lst = ['apple','banana','Apple']

list(filter(lambda x : x[0]== 'A',lst))


# In[25]:


# Filter out the positve number from a list
lst = [1,2,-1,-2]
list(filter(lambda x : x>0 ,lst))


# In[32]:


# filter out the multiples of 3 and 5 from a list
lst = [2,3,5,10,8]
list(filter(lambda x : x%3==0 or x%5==0,lst))


# In[37]:


# find the max string using reuduce function
from functools import reduce
lst = ['madhabi','patra','python_class']
reduce(lambda a,b: a if len(a)>len(b) else b,lst)


# In[47]:


# find the mean , max and min of a given list using reduce function
from functools import reduce
lst = [1,2,3,4,5,6,7,8]
print(reduce(lambda a,b:(a+b)/2,lst))
print(reduce(lambda a,b: a if a>b else b,lst))
print(reduce(lambda a,b: b if a>b else a,lst))


# In[ ]:




