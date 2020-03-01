#!/usr/bin/env python
# coding: utf-8

# In[1]:


list=[1,2,3,4]
list[2]


# In[8]:


## 插入元素：
def insert_elem(array,newelem,location):
    if(location<1|location>len(array)):
        return "ERROR"
    array.append(newelem)
    for nums in range(location,len(array)+1):
        temp=array[nums-1]
        array[nums-1]=newelem
        newelem=temp
    
    return array    
array=[1,2,3,5,6,7]
insert_elem(array,3,5)
        


# In[9]:


##删除元素
array=[1,2,3,5,6,7]
del array[3]
array


# In[12]:


##查找：
def search(array,num):
    for i in range(len(array)):
        result=0
        if array[i]==num:
            return result+1
    return result
array=[1,2,3,4,5,7]
search(array,5)

            


# In[ ]:


# 获取长度
len(array)

