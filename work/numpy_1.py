#!/usr/bin/env python
# coding: utf-8

# In[1]:


def pPrint(arr):
    print('type : {}'.format(type(arr)))
    print('shape : {}, dimension : {}, dtype : {}'.format(arr.shape, arr.ndim, arr.dtype))
    print('넘파이 배열에 저장된 데이터\n', arr)


# In[18]:


import warnings
warnings.filterwarnings('ignore')
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


arr = [1, 2, 3]
np_arr = np.array(arr, dtype=np.int32)
pPrint(np_arr)


# In[5]:


arr = [[1, 2, 3] , [4, 5, 6]]
np_arr = np.array(arr, dtype=np.int32)
pPrint(np_arr)


# In[14]:


data = np.zeros(shape=(2,2), dtype=np.int)
pPrint(data)
data = np.ones(shape=(2,2), dtype=np.int)
pPrint(data)
data = np.full(shape=(3,4), fill_value=25, dtype=np.int)
pPrint(data)
data = np.eye(4)
pPrint(data)
data = np.empty(4)
pPrint(data)


# In[16]:


arr_np = np.arange(1, 10, 3)
pPrint(arr_np)


# In[19]:


data = np.random.normal(100, 10,100)
plt.hist(data, bins=100)
plt.show()

