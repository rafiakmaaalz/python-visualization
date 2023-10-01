#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix


# In[74]:


data=pd.read_csv('IRIS.csv')


# In[75]:


data


# In[76]:


data.head()


# # MATPLOTLIB VISUALIZATION 

# ## SCATTER PLOT

# In[77]:


fig, ax = plt.subplots()


ax.scatter(data['sepal_length'], data['sepal_width'])

ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')


# In[78]:


colors = {'Iris-setosa':'y', 'Iris-versicolor':'g', 'Iris-virginica':'c'}

fig, ax = plt.subplots()

for i in range(len(data['sepal_length'])):
    ax.scatter(data['sepal_length'][i], data['sepal_width'][i],color=colors[data['species'][i]])

ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')


# ## LINECHART

# In[79]:


columns = data.columns.drop(['species'])

x_data = range(0, data.shape[0])

fig, ax = plt.subplots()

for column in columns:
    ax.plot(x_data, data[column])

ax.set_title('Iris Dataset')
ax.legend(['sepal length','sepal width','petal length','petal width'])


# ## BARCHART

# In[80]:


plt.bar(data['species'], data['sepal_length'])
 
plt.title("Iris Dataset")
 

plt.xlabel('Species')
plt.ylabel('Sepal Length')
 

plt.show()


# # SEABORN

# ## SCATTER PLOT

# In[81]:


sns.scatterplot(x='sepal_length', y='petal_width', hue='species', data=data)


# ## LINE CHART

# In[82]:


sns.lineplot(data=data.drop(['species'], axis=1))


# ## PAIRPLOT

# In[83]:


sns.pairplot(data)


# In[88]:


from pandas.plotting import scatter_matrix

fig, ax = plt.subplots(figsize=(10,10))
scatter_matrix(data, alpha=1, ax=ax)


# In[ ]:




