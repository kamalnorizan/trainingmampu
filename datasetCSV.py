#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[99]:


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


# In[83]:


tableSumofIncome = pd.pivot_table(df, values=['ID','Income'], index=['Education'], aggfunc={'ID':'count','Income':'sum'})
tableSumofIncome['avg']=tableSumofIncome['Income']/tableSumofIncome['ID']
tableSumofIncome['additional']=10
print(tableSumofIncome)


# In[106]:


wines = sum(df['MntWines'])
fruits = sum(df['MntFruits'])
meat = sum(df['MntMeatProducts'])
fish = sum(df['MntFishProducts'])
sweet = sum(df['MntSweetProducts'])
gold = sum(df['MntGoldProds'])

data = {'wines': wines, 'fruits': fruits, 'meat':meat, 'fish': fish, 'sweet': sweet, 'gold': gold}
s = pd.Series(data)
df2 = pd.DataFrame(s)
df2['percentage']=df2[0]/sum(s)*100
print(df2)


# In[ ]:




