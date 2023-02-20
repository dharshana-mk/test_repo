#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


#Read the dataset
df = sns.load_dataset('tips')
df.head() 


# #### 1.Create a Line Plot with x (‘total_bill’) versus y (‘tip’) using lineplot() function:

# In[41]:


sns.lineplot(x='total_bill',y='tip',data=df)


# In[36]:


sns.lineplot(x='total_bill',y='tip',data=df,hue='sex',palette='gist_rainbow_r')


# In[ ]:


from the above line plot we can see the contribution of male as well as female
and conclude that males have paid high number of bills compared to females


# #### 2.Create a scatter plot with total_bill and tip 

# In[37]:


sns.scatterplot(x='total_bill',y='tip',data=df,palette='gist_stern_r')


# In[41]:


sns.scatterplot(x='total_bill',y='tip',data=df,hue='day',palette='rocket_r')


# In[ ]:


while we categorise data by day we can visualise the tip on thursday,friday,saturday and sunday and infer that most of the tips
are given on saturday


# #### 3.Write a python code to create a hist plot on total_bill with bins=10.
# - Create the following 
# -Title as "Frequency of Bill Amount"
# -xlabel as "Billed Amount"
# -ylabel as "Count"

# In[68]:


sns.histplot(x='total_bill',palette='prism',data=df,bins=10,hue='sex')
plt.title('Frequency of Bill Amount')
plt.xlabel('Billed Amount')
plt.ylabel('Count')


# In[ ]:


males have paid higher number of bills compared to females.only for the price range 40-50 females have paid on larger counts.


# ## 4.Write a python code to create a heatmap on tips dataset by showing the corelation between numeric attributes 

# In[28]:


sns.heatmap(df.corr())


# In[ ]:


when discussing about the correlation between various numerical data we can analyse nad categorise data as highly correlated,
moderately correlated,lowly correlated.
1.correlation between total bill and size ranges between 0.58-0.63 and it is lowly correlated.we can infer that total bill and 
size have low relationship inbetween them.
2.correlation between tip and size ranges as 0.5 and there is no correlation.we can infer that total bill and 
size doesnot have any relationship inbetween.
3.correlation between total bill and tip ranges between 0.68-0.73 and it is moderately correlated.we can infer that total bill 
and size have moderate relationship inbetween.


# #### 5.Write a python code to create a barplot on smoker and total_bill attribute

# In[64]:


sns.barplot(x='smoker',y='total_bill',data=df,palette='icefire',hue='sex')


# In[ ]:


from the bar plot we can infer that male have paid higher number of bills compared to female in both smoker as well as non 
smoker group.


# #### 6.Write a python code to use the countplot() function to show the count of smokers and non-smokers:

# In[30]:



sns.countplot(x='smoker',data=df,palette='summer_r',hue='sex')


# In[33]:


df['sex'].value_counts()


# In[34]:


df['smoker'].value_counts()


# In[ ]:


as the count of male is double compared to the count of female,population of male is higher in both som


# #### 7.Let’s write a python code to analyze how the tipped amount varies during lunch and dinner time and if there are any outliers in our data. Hint :(Boxplot)

# In[21]:


sns.boxplot(x='tip',y='time',data=df)


# In[ ]:


1.The box plot infers that value around 0.5 is the minimum range,value around 5 is the maximum range,2 is the first quartile range,
value around 3.5 is the third quartile range and 2.2 is the IQR range for the tip in lunch.
2.the box plot infers that value around 0.2 is the minimum range,value around 6 is the maximum range,2 is the first quartile range,
value around 3.8 is the third quartile range and 3 is the IQR range for the tip in dinner.


# #### 8.Let’s write a python code to create a pair plot to show the pair wise distribution of all attributes

# In[35]:


sns.pairplot(df,hue='sex',palette='plasma_r')


# In[ ]:


**********************************THE END*************************

