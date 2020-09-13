#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


print(np.__version__)
print(np.show_config())


# In[8]:


arr = np.zeros(10)
print(arr)


# In[12]:


print("%d bytes" % (arr.size * arr.itemsize))


# In[6]:


get_ipython().run_line_magic('pinfo', 'np.add')


# In[16]:


arr = np.zeros(10)
arr[4] = 1
print(arr)


# In[17]:


arr = np.arange(10,50,7)
print(arr)


# In[20]:


rev = np.flipud(arr)
print(rev)


# In[22]:


arr = np.random.randint(0,9,(3,3))
print(arr)


# In[23]:


arr = np.array([1,2,0,0,4,0])
ans =  np.nonzero(arr)
print(ans)


# In[25]:


iden = np.eye(3,3)
print(iden)


# In[27]:


arr3 = np.random.random((3,3,3))
print(arr3)


# In[29]:


arr = np.random.random((10,10))
a = np.max(arr)
b = np.min(arr)
print("Max:- ",a," Min:- ",b)


# In[30]:


arr = np.random.random((30))
ans = np.mean(arr)
print(ans)


# In[32]:


ans = np.ones((5,5))
ans[1:-1,1:-1] = 0
print(ans)


# In[33]:


ans = np.ones((5,5))
np.pad(ans,pad_width = 1, mode = 'constant',constant_values = 0)


# In[34]:


print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == (3 * 0.1))


# In[35]:


ans = np.diag([1,2,3,4],-1)
print(ans)


# In[36]:


ans = np.zeros((8,8),dtype=int)
ans[1::2,::2] = 1
ans[::2,1::2] = 1
print(ans)


# In[37]:


np.unravel_index(99, (6,7,8))


# In[38]:


arr = [[0,1],[1,0]]
a = 4
b = 4
repetition = (a,b)
ans = np.tile(arr,repetition)
print(ans)


# In[40]:


arr = np.random.rand(5,5)
arr = (arr - np.mean(arr)) / np.std(arr)
print(arr)


# In[43]:


color = np.dtype([("r", np.ubyte, 1),("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),("a", np.ubyte, 1)])


# In[44]:


a = np.random.random((5,3))
b = np.random.random((3,2))
print(np.dot(a,b))


# In[45]:


arr = np.arange(1,10)
arr[(arr>3) & (arr<8)] *=(-1)
print(arr)


# In[46]:


print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))


# In[47]:


legal
legal
legal
legal
legal
illegal


# In[48]:


print(np.array(0) / np.array(0))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))


# In[50]:


Z = np.random.uniform(-10,+10,10)
print(np.copysign(np.ceil(np.abs(Z)), Z))


# In[51]:


arr1 = np.random.randint(0,10,10)
arr2 = np.random.randint(0,10,10)
print(np.intersect1d(arr1,arr2))


# In[52]:


defaults = np.seterr(all="ignore")
Z = np.ones(1)


# In[54]:


np.sqrt(-1) == np.emath.sqrt(-1)


# In[55]:


yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yesterday: ",yesterday)
today = np.datetime64('today', 'D')
print("Today: ",today)
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow: ",tomorrow)


# In[56]:


arr = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(arr)


# In[ ]:




