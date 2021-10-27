#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd

ds = pd.read_csv('D:\pythonTutorial\data.csv', sep='\t')
print(ds)


# In[23]:


# ds.dropna(inplace = True)
new_df = ds.dropna()
print(new_df)


# In[24]:


print(ds)


# In[26]:


nullIncome = pd.isnull(ds['Income'])
ds[nullIncome]


# In[27]:


ds['Income'].fillna(0, inplace = True)


# In[18]:


ds[nullIncome]


# In[28]:


new_df = ds.dropna()
print(new_df)


# In[30]:


# ds.to_csv(r'D:\pythonTutorial\exportedFile.csv', index  =False, header = True)
print(ds)


# In[31]:


ds['Dt_Customer']


# In[36]:


ds['Dt_Customer']=pd.to_datetime(ds['Dt_Customer'], format='%d-%m-%Y', errors='ignore')
print (ds['Dt_Customer'])


# In[37]:


ds


# In[38]:


pd.options.display.max_rows


# In[39]:


ds


# In[40]:


pd.set_option('display.max_rows', None)


# In[41]:


print(ds)


# In[43]:


ds['Dt_Customer']=pd.to_datetime(ds['Dt_Customer'], format='%d-%m-%Y', errors='coerce')
print(ds['Dt_Customer'])


# In[ ]:




