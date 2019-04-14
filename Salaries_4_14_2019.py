#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('Salaries_sample.csv')


# In[3]:


df


# In[4]:


df["Year"].max


# In[5]:


df["Year"].max()


# In[8]:


df[df["Year"]==df["Year"].max()]


# In[11]:


lyt=df[df["Year"]==df["Year"].max()]


# In[12]:


lyt


# In[13]:


lyt.groupby("JobTitle").size()


# In[21]:





# In[19]:





# In[22]:


lyt.groupby('JobTitle')


# In[32]:


g=lyt.groupby('JobTitle')["Salary"].transform('max')


# In[33]:


g


# In[39]:


g.describe()


# In[43]:


lyt.groupby(["JobTitle"])["Salary"].idxmax().values 


# In[53]:


ar=lyt.loc[lyt.groupby(["JobTitle"])["Salary"].idxmax()]


# In[56]:


ar[ar["Salary"]==ar["Salary"].max()]


# In[57]:


ar[ar["Salary"]==ar["Salary"].min()]


# In[63]:


ar.sort_values(by=['Salary'], ascending=False).head(10)


# In[74]:


ar.groupby(['Department']).mean()


# In[ ]:




