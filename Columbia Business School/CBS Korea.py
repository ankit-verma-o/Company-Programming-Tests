#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['font.size'] = 10.0


# ## References for Data
# 
# 1. https://coronaboard.kr/en/
# 2. http://ncov.mohw.go.kr/
# 3. https://hira-covid19.net/
# 4. http://www.cdc.go.kr/contents.es?mid=a30301000000
# 5. https://www.cdc.go.kr/board/board.es?mid=a30402000000&bid=0030
# 6. https://www.worldometers.info/coronavirus/country/south-korea/
# 

# Shutdown is considered on Feb 04, 2020 for this analysis as on this day South Korea imposed travel bans.
# 
# Assumed that Daily Hospitalization cases would be people who died on that day + daily recovered. These two taken because death means extreme case and recovered because of treatment. Although, a patient admitted today will take time to recover but for simplicity, it has been taken that patient admitted will either die or recover the same day.
# 

# ## Entire South Korea

# In[2]:


SKorea=pd.read_excel('Korea.xlsx')
SKorea.head(10)


# In[3]:


len(SKorea)


# In[4]:


x=SKorea['Date']
y=SKorea['Daily Confirmed Cases']
y1=SKorea['Daily Deaths']
y2=SKorea['Daily Recovered']
plt.rcParams["figure.figsize"] = [10,7]
plt.grid(b=True, which='both', axis='both')
plt.plot(x,y, label='Daily Confirmed Cases')
# plt.plot(x,y1, label='Daily Deaths')
plt.plot(x,y2, label='Daily Recovered Cases')
# plt.xticks(rotation=90)
plt.ylabel('Number of Cases')
plt.title('Variation of Daily Confirmed Cases and Daily Recovered Cases with Time')
plt.legend(loc='best')
plt.show()


# In[5]:


x=SKorea['Date']
y1=SKorea['Daily Deaths']
y2=SKorea['Daily Recovered']
plt.rcParams["figure.figsize"] = [10,7]
plt.grid(b=True, which='both', axis='both')
plt.plot(x,y1, label='Daily Deaths')
plt.plot(x,y2, label='Daily Recovered Cases')
# plt.xticks(rotation=90)
plt.ylabel('Number of Cases')
plt.title('Variation of Daily Deaths and Daily Recovered Cases with Time')
plt.legend(loc='best')
plt.show()


# In[6]:


x=SKorea['Date']
y1=SKorea['Total Confirmed Cases']
y2=SKorea['Total Recovered']
y3=SKorea['Total Deaths']
plt.rcParams["figure.figsize"] = [10,7]
plt.grid(b=True, which='both', axis='both')
plt.plot(x,y1, label='Total Confirmed Cases')
plt.plot(x,y2, label='Total Recovered')
plt.plot(x,y3,label='Total Deaths')
# plt.xticks(rotation=90)
plt.ylabel('Number of Cases')
plt.title('Variation of Total Confirmed Cases, Total Recovered Cases and Total Deaths with Time')
plt.legend(loc='best')
plt.show()


# In[7]:


x=SKorea['Date']
y1=SKorea['# of Infected People/Active Cases']
y2=SKorea['Daily Confirmed Cases']
plt.rcParams["figure.figsize"] = [10,7]
plt.grid(b=True, which='both', axis='both')
plt.plot(x,y1, label='# of Infected People/Active Cases')
plt.plot(x,y2, label='Daily Confirmed Cases')
plt.ylabel('Number of Active Cases')
plt.title('Variation of Number of Infected People and Daily Confirmed Cases with Time')
plt.legend(loc='best')
plt.show()


# In[8]:


x=SKorea['Date']
y1=SKorea['Daily Confirmed Cases']
y2=SKorea['Daily Hospitalization']
plt.rcParams["figure.figsize"] = [10,7]
plt.grid(b=True, which='both', axis='both')
plt.plot(x,y1, label='Daily Infection ')
plt.plot(x,y2, label='Daily Hospitalization')
plt.ylabel('Number of Active Cases')
plt.title('Variation of Daily Infection and Daily Hospitalization with Time')
plt.legend(loc='best')
plt.show()


# ## Seoul Province

# In[9]:


Seoul=pd.read_excel('Seoul.xlsx')
Seoul.head()


# In[10]:


len(Seoul)


# In[11]:


x=np.arange(1,103)
y1=Seoul['Daily Confirmed Cases']
y2=Seoul['Daily Hospitalization']
plt.rcParams["figure.figsize"] = [10,7]
plt.grid(b=True)
plt.plot(x,y1, label='Daily Infection ',color='red')
plt.plot(x,y2, label='Daily Hospitalization',color='black')
plt.xlabel('Number of Days Since Jan 20,2020')
plt.ylabel('Number of Active Cases')
plt.title('Variation of Daily Infection and Daily Hospitalization with Time')
plt.legend(loc='best')
# plt.xticks(rotation=90)
plt.show()


# In[12]:


x=np.arange(1,103)
y1=Seoul['Total Confirmed Cases']
y2=Seoul['Total Recovered']
y3=Seoul['Total Deaths']
plt.rcParams["figure.figsize"] = [10,7]
plt.grid(b=True)
plt.plot(x,y1, label='Total Confirmed Cases')
plt.plot(x,y2, label='Total Recovered')
plt.plot(x,y3,label='Total Deaths')
# plt.xticks(rotation=90)
plt.ylabel('Number of Cases')
plt.title('Variation of Total Confirmed Cases, Total Recovered Cases and Total Deaths with Time')
plt.legend(loc='best')
plt.show()


# In[ ]:




