#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Importing libraries


# In[1]:


import pandas as pd


# In[18]:


weather_data = pd.read_csv(r'C:\Users\USER\Downloads\1. Weather Data.csv')


# In[ ]:


#Data Exploration


# In[19]:


weather_data


# In[20]:


pd.options.display.max_columns = None
pd.options.display.max_rows = None


# In[21]:


display(weather_data)


# In[63]:


weather_data.copy()


# In[23]:


weather_data.info()


# In[25]:


weather_data.shape


# In[27]:


weather_data.head(5)


# In[28]:


weather_data.columns


# In[29]:


weather_data['Weather'].unique()


# In[30]:


weather_data.nunique()


# In[32]:


weather_data.count()


# In[34]:


weather_data['Weather'].value_counts()


# In[35]:


weather_data.columns


# In[37]:


weather_data['Wind Speed_km/h'].unique()


# In[38]:


weather_data.nunique()


# In[40]:


weather_data['Weather'].value_counts()


# In[43]:


weather_data.groupby('Weather').get_group('Clear')


# In[44]:


weather_data.head(3)


# In[48]:


weather_data.groupby('Wind Speed_km/h').get_group(4)


# In[55]:


weather_data.isnull().sum()


# In[61]:


weather_data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)


# In[62]:


weather_data


# In[64]:


weather_data.Visibility_km.mean()


# In[67]:


weather_data.columns


# In[68]:


weather_data.Press_kPa.std()


# In[70]:


weather_data[weather_data['Weather Condition'] == 'Snow']


# In[73]:


weather_data[weather_data['Weather Condition'].str.contains('Snow')].head(10)


# In[76]:


weather_data[(weather_data['Wind Speed_km/h'] > 24) & (weather_data['Visibility_km'] == 25)]


# In[77]:


weather_data.groupby('Weather Condition').mean()


# In[78]:


weather_data.groupby('Weather Condition').min()


# In[80]:


weather_data.groupby('Weather Condition').max()


# In[81]:


weather_data.groupby('Weather Condition').get_group('Fog')


# In[82]:


weather_data.head(2)


# In[87]:


weather_data['Weather Condition'].value_counts()


# In[88]:


weather_data.columns


# In[89]:


weather_data[(weather_data['Weather Condition'] == 'Clear') | (weather_data['Visibility_km'] > 40)]


# In[90]:


weather_data.head(3)


# In[93]:


weather_data[(weather_data['Weather Condition'] =='Clear') & (weather_data['Rel Hum_%'] > 50) | (weather_data['Visibility_km'] > 40)]


# In[ ]:




