#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd


# In[14]:


df=pd.read_excel('C:/Users/mkdha/OneDrive/Desktop/hv/Bank Personal Loan Modelling.xlsx','Data')


# In[15]:


df


# In[16]:


import numpy as np


# In[5]:


#1. The average selling price of a food item in the restaurant is Rs 250.00, and the standard 
#deviation of the price is Rs 47.00. The median value is an indication of the central value of the 
#data and is close to the mean of Rs 202.00. If you have to be a customer of this shop will you be 
#a regular customer?

mean=Rs.250
sd=Rs.47
median=mean of 202
EXPLANATION:
#1.being a regular customer for the respective restaurant will be difficult as the average selling price is Rs.250 which is not
#affordable in a daily basis.
#2.I can be a regular customer for fancy or occasional lunch/dinner at the respective restaurant if 
# the taste of the foods are price worthy.


# 

# In[21]:


#2.In a residential locality, the average size of the house is 2224 square feet, with a standard 
#deviation of 248 sq feet which indicates that the distribution of size is fairly the same across the 
#data and the median value of the house is 2220 square feet. Does the locality have any 
#bigger/smaller-sized houses?

avg size=2224 sqft
sd=248 sqft
median=2220 sqft
EXPLANATION:
#1.As the average size of house is 2224 sqft and the standard deviation is also low,the sizes of the house are approximately
# similar.
#2.I would conclude that the average size as 2224 sqft is capable of building similar bigger size houses.


# In[ ]:





# In[6]:


#3.You want to invest money in buying a house. Now you have the data belonging to locality X and 
#locality Y. Some of the house prices in locality X are 2.00 L,10.00 L, 8.00 L, and 12.00 L and the 
#prices belonging to Y are 2.5 L, 9.50 L, 8.15 L, and 12.50 L. Now you have to take a statistical 
#measure to decide which locality will be best for the investment
#X=[2,10,8,12] in lakhs
#Y=[2.5,9.5,8.15,12.5] in lakhs
x=np.array([2,10,8,12])
y=np.array([2.5,9.5,8.15,12.5])
m=np.mean(x)
n=np.mean(y)
print('MEAN OF X IS ',m)
print('MEAN OF Y IS',n)


# In[ ]:


EXPLANATION.Q.3
#1.as average price of  Y is greater than X (8.1625L > 8L).
#2.The value of land in Y locality is higher and will be multiplied quickly in near future also
#3.Hence i would like to invest money in Y locality.


# In[ ]:





# In[23]:


#4.During the survey, the ages of 80 patients infected by COVID and admitted to one of the city
#hospitals were recorded and the collected data is represented in the less than cumulative 
#frequency distribution table.
Age (in yrs.) No. of Patients
5 - 15              6
15 - 25            11
25 - 35            21
35 - 45            23
45 - 55            14
55 - 65             5
#a. Which class interval has the highest frequency?
23 is the highest frequency and it belongs to age group 35-45
#b. Which age was affected the least?
5 is the least number of affected patients and it belongs to group 55-65
#c. How many patients of age 45 years and above were admitted?
19 (14+5) were admitted in the age of 45yrs and above
#d. Which is the modal class interval in the above dataset
35-45
#e. What is the median class interval of age?
30-40


# In[ ]:





# In[24]:


#5.Assume you are the trader and you have invested over the years, and you are worried about the 
#average return on investment. What average method you would use to compute the average 
#return for the data given below?
finding average of investment and return


# In[ ]:





# In[25]:


#6.Suppose you have been told to measure all the heights of the male on the earth. What would be 
#your strategy for the measure?
I prefer heights to be measured in feets and mean to be the best way to compare the heights of every male on earth


# In[ ]:





# In[48]:


#7. Calculate the z score of the following numbers:
#X = [4.5,6.2,7.3,9.1,10.4,11]

m=np.array([4.5,6.2,7.3,9.1,10.4,11])
mn=np.mean(m)
sd=np.std(m)


# In[51]:


m=np.array([4.5,6.2,7.3,9.1,10.4,11])
for i in m:
    z_score=(i-mn)/sd
    print('z score is' ,z_score)


# In[ ]:





# In[21]:


#8. Give us the statistical summary for all the variables in the dataset.
summary=df.describe()
print(summary)


# In[ ]:





# In[41]:


#9. Give all the measures of central tendency for all the quantitative variables which are continuous 
# and also discrete.
mean=df[['Age','Experience','Income','Family','CCAvg','Mortgage']].mean()
print(mean)


# In[42]:


median=df[['Age','Experience','Income','Family','CCAvg','Mortgage']].median()
print(median)


# In[43]:


mode=df[['Age','Experience','Income','Family','CCAvg','Mortgage']].mode()
print(mode)


# In[ ]:





# In[6]:


#10. Can you apply any statistical method to observe any similarity in distribution between age and 
# experience variables?
df[['Age','Experience']].corr()


# In[ ]:





# In[44]:


#11. Who are the most frequent family members present in this dataset?
df['Family'].mode()


# In[ ]:





# In[39]:


#12. What is the percentage of variation you can observe in the ‘Income’ variable
income_std = df["Income"].std()
income_mean =df["Income"].mean()
percent_var = (income_std/income_mean)*100
percent_var


# In[ ]:





# In[36]:


#13. The ‘Mortgage’ variable is having a lot of zeroes. Impute with some business logical value that 
# you feel fit for the data.
impute_zeros = df.replace(0.0,df["Mortgage"].mean())
impute_zeros


# In[38]:


impute_zeros.nunique()


# In[ ]:


#EXPLANATION
There are 347 unique values in mortgage variable.i.e.,346 unique and one mean value(56.498) which is replaced for zeroes.


# In[53]:


#14. Do customers have credit cards have any impact on their experience and income?
s=df[df['CreditCard']==1]
w=s['Income'].mean()
print('average income of customers with credit card is ',w)
y=s['Experience'].mean()
print('average experience of customers with credit cards is ',y)


# In[ ]:


#EXPLANATION
credit cards doesnot hold any impact neither on experience nor on income.
instead,experience only have impact on the income. 


# In[21]:


#15. Do you see any outliers in the dataset? If yes what plot you would think will be suitable to 
#showcase to the stakeholders
a=df[['Age','Experience','Income','Family','CCAvg','Mortgage']].skew()
a


# In[27]:


a=df[['Age','Experience','Income','Family','CCAvg','Mortgage']].plot(kind='box')
print(a)


# In[ ]:


HIGHLY SKEWED
Mortgage               2.104002
CCAvg                  1.598457
Age                   -0.029341
Experience            -0.026325

MODERATELY SKEWED
Income                 0.841339
Family                 0.155221


# In[ ]:


#EXPLANATION
As mortgage,CCavg,age,experience are highly skewed hence outliers are maximum in these variable.


# In[59]:


#16. Give us the deciles values of the variable ‘Income’ in the dataset.
df['DecileRank']=pd.qcut(df['Income'],q=10,labels=False)
print(DecileRank)


# In[ ]:





# In[57]:


#17. Give the IQR of all the variables which are quantitative and continuous.
#Experience
q1 = df['Experience'].quantile(.25)
q3 = df['Experience'].quantile(.75)
mask = df['Experience'].between(q1, q3, inclusive=True)
iqr = df.loc[mask, 'Experience']
print(iqr)


# In[59]:


#Income
q1 = df['Income'].quantile(.25)
q3 = df['Income'].quantile(.75)
mask = df['Income'].between(q1, q3, inclusive=True)
iqr = df.loc[mask, 'Income']
print(iqr)


# In[60]:


#ccavg
q1 = df['CCAvg'].quantile(.25)
q3 = df['CCAvg'].quantile(.75)
mask = df['CCAvg'].between(q1, q3, inclusive=True)
iqr = df.loc[mask, 'CCAvg']
print(iqr)


# In[ ]:





# In[65]:


#MORTGAGE
q1 = df['Mortgage'].quantile(.25)
q3 = df['Mortgage'].quantile(.75)
mask = df['Mortgage'].between(q1, q3, inclusive=True)
iqr = df.loc[mask, 'Mortgage']
print(iqr)


# In[ ]:





# In[40]:


#18. Do the higher-income holders spend more on credit cards?
higher_income_holders=df[df['Income']>75]
s=higher_income_holders.mean()
print(s)


# In[41]:


higher_income_holders=df[df['Income']<75]
s=higher_income_holders.mean()
print(s)


# In[ ]:


#EXPLANATION
Mean of CCavg is 2.979 for people with income greater than 75k and mean of CCavg for people with
income less than 75k is 1.209 which is comparatively low.
Hence I conclude that higher income holders with mean 2.979 spend more on credit cards.


# In[ ]:





# In[22]:


#19. Do customers using bank internet facilities paid higher?
net=df[df['Online']==1.0]
net.sort_values('Income',ascending=False)


# In[ ]:


#EXPLANATION:Q19
seeing the salaries of the people with credit card we can predict that people with credit card are also paid higher.


# In[16]:


#20. Calculate the Z score of the ‘income’ variable.
mean=df['Income'].mean()
sd=df['Income'].std()
z_score=(df['Income']-mean)/sd
print(z_score)


# In[ ]:





# In[8]:





# In[ ]:




