#!/usr/bin/env python
# coding: utf-8

# In[13]:


#********************WEEK4_ACT3_EX1***********************************
import numpy as np
import pandas as pd
#opening the file
df=pd.read_csv("PeoplesFavourites.csv")
df


# In[14]:


#QUESTION 1
#remove customer names (first and last), replacing with a unique identifier. 
#We will be using lambda to generate unique keys

df["First Name"]=df["First Name"].apply(lambda a:abs(hash(a)))
df["Last Name"]=df["Last Name"].apply(lambda a:abs(hash(a)))
df


# In[19]:


#QUESTION 2 - null values and consistency
#I will treat 0 (string), none, 0, '' as null values

df=df.replace(0,"null")
df=df.replace("none","null")
df=df.replace('',"null")
df=df.replace("0","null")
df


# In[16]:


#QUESTION 3
#Removing any customer data that has missing data in any of the following:
#first, last and email



# In[20]:


df=df.dropna(subset=["First Name","Last Name","Email"])
df


# In[22]:


#Question 4 - exporting the data
df=df.to_csv('newdata.csv')

