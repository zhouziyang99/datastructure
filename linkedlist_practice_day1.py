#!/usr/bin/env python
# coding: utf-8

# In[1]:


##定义一个linked list的类
#节点
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
#末位
class LinkedListOneway(object):
    def __init__(self, node=None):
        self.__head = node
        
##遍历
    def __len__(self):
        cur = self.__head
        while cur:
            cur = cur.next
        return "complete"


# In[2]:


##插入元素
    def insert(self, location, value):
        if location <= 0:#check
            return "ERROR"
        elif location > len(self) - 1:
            return "ERROR"
        else:
            node = Node(value)
            prior = self.__head
            num = 0
            while count < (location - 1):
                prior = prior.next
                num += 1
            node.next = prior.next
            prior.next = node


# In[ ]:


##删除元素
    def remove(self, value):
        cur = self.__head
        prior = None
        while cur:
            if value == cur.value:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    prior.next = cur.next
                break
            else:
                prior = cur
                cur = cur.next


# In[ ]:


##查找
    def search(self, value):
        cur = self.__head
        while cur:
            if value == cur.value:
                return 1
            cur = cur.next
        return "ERROR"


# In[ ]:


##获取
    self.value()

