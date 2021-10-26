#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[31]:


import pandas as pd
import numpy as np
df = pd.read_csv('D:\pythonTutorial\data.csv', sep='\t')
print(df)
print(df.loc[:,['ID','Year_Birth','Income']])
print(df.iloc[10])


# In[15]:


print(df.iloc[:,[0]])


# In[28]:


print(df.iloc[:, :6])


# In[29]:


print(df.loc[:10,['ID','Year_Birth','Income']])


# In[45]:


table = pd.pivot_table(df, values = 'ID', index=['Marital_Status'], aggfunc='count')
print(table)


# In[47]:


print(df)


# In[48]:


table = pd.pivot_table(df, values='ID', index=['Marital_Status'], aggfunc='count' )
print(table)


# In[59]:


tableSumofIncome = pd.pivot_table(df, values=['ID','Income'], index=['Education'], aggfunc={'ID':'count','Income':'sum'})
print(tableSumofIncome)


# In[ ]:




