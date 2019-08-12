#!/usr/bin/env python
# coding: utf-8

# In[6]:


""" ---------------------------------
 
  呼び出し練習用 class
 
   ----------------------------------
""" 
class SampleClass:
    num1 = 0
    str1 = ""
    def __init__(self):
        self.num1 = 10
        self.str1 = "abc"
        
    def printNum(self):
        print(self.num1)
        
    def printStr(self):
        print(self.str1)

