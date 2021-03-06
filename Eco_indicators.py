
# coding: utf-8

# # In this Script I used the data from Germany that includes the Economic indicators between 1980-2020
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **economic activity or measures** (see below) for the region of **Mainz, Rheinland-Pfalz, Germany**, or **Germany** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Mainz, Rheinland-Pfalz, Germany** to Ann Arbor, USA. In that case at least one source file must be about **Mainz, Rheinland-Pfalz, Germany**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Mainz, Rheinland-Pfalz, Germany** and **economic activity or measures**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **economic activity or measures**?  For this category you might look at the inputs or outputs to the given economy, or major changes in the economy compared to other regions.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[1]:

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib notebook')
plt.style.use('seaborn-colorblind')
population=pd.read_excel('Population.xlsx',skiprows=35,header=None).rename(columns={0:'index',1:'Pop'})
indicators=pd.read_csv('Eco_indicators.csv',skiprows= [4,5],usecols=(list(range(5,46))))
indicators=indicators.T.rename(columns={0:'GDP',1:'Inflation',2:'Unemployment_percent'}).reset_index()
indicators['Unemployment']=None
for i in range(1,len(indicators)):
    indicators.loc[i,'Unemployment']=indicators.loc[i-1,'Unemployment_percent']-indicators.loc[i,'Unemployment_percent']

Eco_indicators=pd.DataFrame(indicators[['Inflation','GDP','Unemployment','index']]).rename(columns={'index':'Dates'}).set_index('Dates')
population['Pop_change']=None
for i in range(1,len(population)):
    population.loc[i,'Pop_change']=round(((population.loc[i,'Pop']-population.loc[i-1,'Pop'])/population.loc[i-1,'Pop'])*100,2)
Pop_change=pd.DataFrame(population[['Pop_change']]).set_index(Eco_indicators.index)
Final_eco=pd.merge(Pop_change,Eco_indicators,how='outer',left_index=True,right_index=True)

Final_eco.plot(figsize=(10,8),colormap='viridis',grid=False).set_facecolor('white')
plt.title('Economic Indicators of Germany between 1980 and 2020 \n (Percent Change with respect to previous year)')
plt.xlabel('Dates')
plt.ylabel('Percent Change (%)')
plt.axhline(y=0,color='black',linestyle='--')
for i in [-8,-5,5,10,15,20]:
    plt.axhline(y=i,color='black',linestyle='--',alpha=0.06)
strtext='Year 1990: Berlin Wall collapse \nYear 2020: Estimations gathered from imf.org '
plt.text(26,18, strtext,bbox=dict(boxstyle='round', facecolor='white', alpha=0.1))
plt.savefig('Assignment4.jpg')


# In[ ]:



