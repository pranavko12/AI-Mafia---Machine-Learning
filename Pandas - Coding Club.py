#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[8]:


imdb_df = pd.read_csv("Downloads/imdb_1000.csv")


# In[9]:


imdb_df.head()


# In[13]:


bikes_df = pd.read_csv("Downloads/bikes.csv", sep = ";", parse_dates = ['Date'], dayfirst = True, index_col = 'Date')


# In[14]:


bikes_df.head()


# In[15]:


bikes_df.head(3)


# In[17]:


imdb_df.columns


# In[18]:


imdb_df.dtypes


# In[19]:


imdb_df['title'].head(5)


# In[20]:


imdb_df[['title', 'genre']].head()


# In[21]:


imdb_df.duration.dtype


# In[22]:


imdb_df.duration.values[:10]


# In[23]:


imdb_df['title'].apply(lambda x:x.upper()).head()


# In[24]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


bikes_df['Berri1'].plot()


# In[26]:


bikes_df.plot(figsize=(12,6))


# In[27]:


imdb_df['genre'].value_counts()


# In[28]:


imdb_df['genre'].value_counts().plot.bar()


# In[29]:


bikes_df.loc['2012-01-01']


# In[31]:


imdb_df.iloc[10]


# In[32]:


imdb_df[imdb_df['genre'] == 'Adventure'].head()


# In[33]:


good_movie = (imdb_df['star_rating'] > 8) & (imdb_df['duration'] > 130)


# In[35]:


imdb_df[good_movie]['genre'].value_counts()


# In[36]:


bikes_df['weekday'] = bikes_df.index.weekday


# In[37]:


bikes_df.head()


# In[38]:


bikes_df.drop('Unnamed: 1', axis=1, inplace=True)


# In[39]:


bikes_df.head()


# In[45]:


genre_groups = imdb_df.groupby('genre')
genre_groups.get_group('Crime').head()


# In[46]:


genre_groups.aggregate('mean')


# In[47]:


imdb_df['new_duration'] = genre_groups['duration'].transform(lambda x:x.mean())


# In[48]:


imdb_df.head()


# In[49]:


weekday_groups = bikes_df.groupby('weekday')
weekday_counts = weekday_groups.aggregate(sum)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# In[50]:


weekday_counts['Berri1'].plot.bar()


# In[ ]:




