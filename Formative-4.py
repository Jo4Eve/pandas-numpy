#!/usr/bin/env python
# coding: utf-8

# In[254]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[73]:


import csv
from csv import DictReader
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#use pandas to read the data
airport = pd.read_csv('airports.csv')

# creating a new csv file excluding data with word 'closed'
newFile = airport[(airport['type'] != 'closed')]
newFile.to_csv('newAirportData.csv')
newAirportfile = pd.read_csv('newAirportData.csv', usecols = ('iso_country','type','ident','id' ))
newAirportfile

# filtering the new file out for GB airports
GBfile = newAirportfile[(newAirportfile['iso_country'] == 'GB')]

# this pivots data in columns 'type' into rows
pivoted = GBfile.pivot(index = ('ident','iso_country'), columns = 'type', values = 'id')

#specifying which columns to be headers
file1 = pivoted.to_csv('pivotedData.csv')
file2 = pd.read_csv('pivotedData.csv', usecols = ('ident','small_airport','medium_airport','large_airport'))
file2


#open the frequency file and merge columns with same data together
freq = pd.read_csv('airport-frequencies.csv', usecols = ['airport_ident' ,'id', 'frequency_mhz'])
# freq2 = freq.pivot(index = 'id', columns = 'frequency_mhz', values = 'airport_ident')
# freq2

#this merges airport data using the 'ident' column which matches frequecy file 'airport_ident'
airportPlusfreq = pd.merge(file2, freq, left_on = 'ident',right_on =  'airport_ident')
airportPlusfreq
#adding the runways file data  
runways = pd.read_csv('runways.csv')

#the three data files
threeFilesMerged = pd.merge(airportPlusfreq, runways, left_on = "airport_ident", right_on = "airport_ident")
threeFilesMerged2 = threeFilesMerged.to_csv('threeFiles.csv')

finalFile = pd.read_csv('threeFiles.csv', usecols  = ('frequency_mhz','ident','large_airport','medium_airport',
                                                      'small_airport'))
finalFile2 = finalFile.to_csv('finalFile.csv',index = False,)

file = pd.read_csv('finalFile.csv')
#final_file = file.drop_duplicates('ident')
#file2 = final_file.pivot(index = ['ident','iso_country'],values = ['large_airport'
#  #                             ,'medium_airport','small_airport'], columns = ['frequency_mhz',]) 
grouped = file['frequency_mhz'].groupby(file['large_airport']) 
print(grouped.mean())
grouped.median()
file.T
#sns.barplot(x = 'frequency_mhz',y =['large_airport','medium_airport','small_airport'], data = file)


# ### converting the final file to JSON format                               

# In[1]:


jsonFile = file.to_json (orient= 'index',indent = 2) 

print (jsonFile)
        
        


# In[228]:


import csv
from csv import DictReader
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#use pandas to read the data
airport = pd.read_csv('airports.csv')
runways = pd.read_csv('runways.csv')
freq = pd.read_csv('airport-frequencies.csv')


# creating a new csv file excluding data with word 'closed'
airport_without_closed = airport[airport['type'] != 'closed']

#display only GB airports without closed 'type'
airport_GB = airport[airport['iso_country'] == 'GB'].merge(airport_without_closed)

#merge airport and the frequencies files
airport_GB_merged = pd.merge(airport_GB,freq, left_on = 'ident', right_on = 'airport_ident')

#filter columns to display
airport_files = airport_GB_merged.loc[:, ['name','ident','type_x','frequency_mhz']]
airport_files

#convert airport type into columns and fill in their respective frequencies
cross_tab = pd.crosstab( airport_files.name,airport_files.type_x,
                        values =airport_files.frequency_mhz,aggfunc ='count',colnames = ['Size of Airport'],
                        rownames = ['Name of Airport'],margins_name = 'Total', margins  = True)
cross_tab['medium_airport'].mean()
#filter columns to display

# file = airport_files.pivot_table(index = ['frequency_mhz'], columns =['type_x']
#,values = 'ident',aggfunc = 'first' )
# file.reset_index(inplace = True)
# file

# #grouped = file['frequency_mhz'].groupby(file['large_airport'])
# types_to_columns = file.loc[:,['frequency_mhz','large_airport','medium_airport','small_airport']]

# types_to_columns
# # grouped = types_to_columns.groupby(types_to_columns['large_airport'])['frequency_mhz']
# # grouped.mean()
# # types_to_columns['large_airport'].mean
# # # grouped.median()
# # # types_to_columns.dtypes
# # # grouped.mean()


# In[ ]:





# In[ ]:




