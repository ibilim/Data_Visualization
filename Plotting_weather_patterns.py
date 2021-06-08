

# # Visualising Max Min Temperature values between 2005 and 2016
# Each row in the assignment datafile corresponds to a single observation.
# 
# The following variables are provided to you:
# 
# * **id** : station identification code
# * **date** : date in YYYY-MM-DD format (e.g. 2012-01-24 = January 24, 2012)
# * **element** : indicator of element type
#     * TMAX : Maximum temperature (tenths of degrees C)
#     * TMIN : Minimum temperature (tenths of degrees C)
# * **value** : data value for element (tenths of degrees C)
# 
# For this assignment, you must:
# 
# 1. Read the documentation and familiarize yourself with the dataset, then write some python code which returns a line graph of the record high and record low temperatures by day of the year over the period 2005-2014. The area between the record high and record low temperatures for each day should be shaded.
# 2. Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015.
# 3. Watch out for leap days (i.e. February 29th), it is reasonable to remove these points from the dataset for the purpose of this visualization.
# 4. Make the visual nice! Leverage principles from the first module in this course when developing your solution. Consider issues such as legends, labels, and chart junk.
# 
# The data you have been given is near **Ann Arbor, Michigan, United States**, and the stations the data comes from are shown on the map below.

# In[1]:

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd


def leaflet_plot_stations(binsize, hashid):

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8,8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return mplleaflet.display()

leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')


# In[2]: import Cvs data in python and opens the data

%matplotlib notebook
import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np
df1=pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
df1['Data_Value']=df1['Data_Value']/10


# In[3]:

import numpy as np
tmax=df1[df1['Element']=='TMAX'][['Date','Data_Value']]   # 
tmax=tmax[tmax['Date']<'2015'].sort_values(['Date']).drop_duplicates(keep='first').reset_index()
date_list_max=[]
temp_temporary=[]
temp_list_max=[]
for i in range(len(tmax.index)):
    if i+1 not in tmax.index:
        temp_temporary.append(tmax.loc[i,'Data_Value'])
        temp_list_max.append(np.array(temp_temporary).max())
        date_list_max.append(tmax.loc[i,'Date'])
        break
    if tmax.loc[i,'Date']==tmax.loc[i+1,'Date']:
        temp_temporary.append(tmax.loc[i,'Data_Value'])
    else:
        temp_temporary.append(tmax.loc[i,'Data_Value'])
        temp_list_max.append(np.array(temp_temporary).max())
        date_list_max.append(tmax.loc[i,'Date'])
        temp_temporary=[]
        continue
df_max=pd.DataFrame(temp_list_max,date_list_max).reset_index().rename(columns={'index':'Date',0:'Temp'})


# In[5]:

tmin=df1[df1['Element']=='TMIN'][['Date','Data_Value']]
tmin=tmin[tmin['Date']<'2015'].sort_values(['Date']).drop_duplicates(keep='first').reset_index()
date_list_min=[]
temp_list_temporary=[]
temp_list_min=[]
for i in range(len(tmin.index)):
    if i+1 not in tmin.index:
        temp_list_temporary.append(tmin.loc[i,'Data_Value'])
        temp_list_min.append(np.array(temp_list_temporary).min())
        date_list_min.append(tmin.loc[i,'Date'])
        break
    if tmin.loc[i,'Date']==tmin.loc[i+1,'Date']:
        temp_list_temporary.append(tmin.loc[i,'Data_Value'])
    else:
        temp_list_temporary.append(tmin.loc[i,'Data_Value'])
        temp_list_min.append(np.array(temp_list_temporary).min())
        date_list_min.append(tmin.loc[i,'Date'])
        temp_list_temporary=[]
        continue
df_min=pd.DataFrame(temp_list_min,date_list_min).reset_index().rename(columns={'index':'Date',0:'Temp'})

# In[6]:

tmin_2015=df1[df1['Element']=='TMIN'][['Date','Data_Value']]
tmin_2015=tmin_2015[tmin_2015['Date']>'2014-12-31'].sort_values(['Date']).drop_duplicates(keep='first').reset_index()
#tmin_2015=tmin_2015.drop_duplicates(keep='first').reset_index()
date_2015_min=[]
temp_2015=[]
tempmin_2015=[]
for i in range(len(tmin_2015.index)):
    if i+1 not in tmin_2015.index:
        temp_2015.append(tmin_2015.loc[i,'Data_Value'])
        tempmin_2015.append(np.array(temp_2015).min())
        date_2015_min.append(tmin_2015.loc[i,'Date'])
        break
    if tmin_2015.loc[i,'Date']==tmin_2015.loc[i+1,'Date']:
        temp_2015.append(tmin_2015.loc[i,'Data_Value'])
    else:
        temp_2015.append(tmin_2015.loc[i,'Data_Value'])
        tempmin_2015.append(np.array(temp_2015).min())
        date_2015_min.append(tmin_2015.loc[i,'Date'])
        temp_2015=[]
        continue

tmax_2015=df1[df1['Element']=='TMAX'][['Date','Data_Value']]
tmax_2015=tmax_2015[tmax_2015['Date']>'2014-12-31'].sort_values(['Date']).drop_duplicates(keep='first').reset_index()

date_2015_max=[]
temp_2015_temporary=[]
tempmax_2015=[]
for i in range(len(tmax_2015.index)):
    if i+1 not in tmax_2015.index:
        temp_2015_temporary.append(tmax_2015.loc[i,'Data_Value'])
        tempmax_2015.append(np.array(temp_2015_temporary).min())
        date_2015_max.append(tmax_2015.loc[i,'Date'])
        break
    if tmin_2015.loc[i,'Date']==tmax_2015.loc[i+1,'Date']:
        temp_2015_temporary.append(tmax_2015.loc[i,'Data_Value'])
    else:
        temp_2015_temporary.append(tmax_2015.loc[i,'Data_Value'])
        tempmax_2015.append(np.array(temp_2015_temporary).min())
        date_2015_max.append(tmax_2015.loc[i,'Date'])
        temp_2015_temporary=[]
        continue
print(tempmax_2015)


# In[7]:

dfm5=df_max[df_max['Date']<'2006'] #.rename(columns={'Temp':'Tmax_2005'})
dfm6=df_max[(df_max['Date']>'2005-12-31') & (df_max['Date']<'2007')].reset_index()#.rename(columns={'Temp':'Tmax_2006'})
dfm7=df_max[(df_max['Date']>'2006-12-31') & (df_max['Date']<'2008')].reset_index()#.rename(columns={'Temp':'Tmax_2007'})
dfm8=df_max[(df_max['Date']>'2007-12-31') & (df_max['Date']<'2009')].reset_index()#.rename(columns={'Temp':'Tmax_2008'})
dfm9=df_max[(df_max['Date']>'2008-12-31') & (df_max['Date']<'2010')].reset_index()#.rename(columns={'Temp':'Tmax_2009'})
dfm10=df_max[(df_max['Date']>'2009-12-31') & (df_max['Date']<'2011')].reset_index()#.rename(columns={'Temp':'Tmax_2010'})
dfm11=df_max[(df_max['Date']>'2010-12-31') & (df_max['Date']<'2012')].reset_index()#.rename(columns={'Temp':'Tmax_2011'})
dfm12=df_max[(df_max['Date']>'2011-12-31') & (df_max['Date']<'2013')].reset_index()#.rename(columns={'Temp':'Tmax_2012'})
dfm13=df_max[(df_max['Date']>'2012-12-31') & (df_max['Date']<'2014')].reset_index()#.rename(columns={'Temp':'Tmax_2013'})
dfm14=df_max[df_max['Date']>'2013-12-31'].reset_index()#.rename(columns={'Temp':'Tmax_2014'})

tmax2015_to_show=[]
for i in range(len(dfm5.index)):
    if tempmax_2015[i]>np.array([dfm5.loc[i,'Temp'],dfm6.loc[i,'Temp'],dfm7.loc[i,'Temp'],
                                dfm8.loc[i,'Temp'],dfm9.loc[i,'Temp'],dfm10.loc[i,'Temp'],
                                dfm11.loc[i,'Temp'],dfm12.loc[i,'Temp'],dfm13.loc[i,'Temp'],
                                dfm14.loc[i,'Temp']]).max():
        tmax2015_to_show.append(tempmax_2015[i])
print(tmax2015_to_show)

dfmin5=df_min[df_min['Date']<'2006'] #.rename(columns={'Temp':'Tmax_2005'})
dfmin6=df_min[(df_min['Date']>'2005-12-31') & (df_min['Date']<'2007')].reset_index()#.rename(columns={'Temp':'Tmax_2006'})
dfmin7=df_min[(df_min['Date']>'2006-12-31') & (df_min['Date']<'2008')].reset_index()#.rename(columns={'Temp':'Tmax_2007'})
dfmin8=df_min[(df_min['Date']>'2007-12-31') & (df_min['Date']<'2009')].reset_index()#.rename(columns={'Temp':'Tmax_2008'})
dfmin9=df_min[(df_min['Date']>'2008-12-31') & (df_min['Date']<'2010')].reset_index()#.rename(columns={'Temp':'Tmax_2009'})
dfmin10=df_min[(df_min['Date']>'2009-12-31') & (df_min['Date']<'2011')].reset_index()#.rename(columns={'Temp':'Tmax_2010'})
dfmin11=df_min[(df_min['Date']>'2010-12-31') & (df_min['Date']<'2012')].reset_index()#.rename(columns={'Temp':'Tmax_2011'})
dfmin12=df_min[(df_min['Date']>'2011-12-31') & (df_min['Date']<'2013')].reset_index()#.rename(columns={'Temp':'Tmax_2012'})
dfmin13=df_min[(df_min['Date']>'2012-12-31') & (df_min['Date']<'2014')].reset_index()#.rename(columns={'Temp':'Tmax_2013'})
dfmin14=df_min[df_min['Date']>'2013-12-31'].reset_index()#.rename(columns={'Temp':'Tmax_2014'})

tmin2015_to_show=[]
tmin2015_date_to_show=[]
for i in range(len(dfmin5.index)):
    if tempmin_2015[i]<np.array([dfmin5.loc[i,'Temp'],dfmin6.loc[i,'Temp'],dfmin7.loc[i,'Temp'],
                                dfmin8.loc[i,'Temp'],dfmin9.loc[i,'Temp'],dfmin10.loc[i,'Temp'],
                                dfmin11.loc[i,'Temp'],dfmin12.loc[i,'Temp'],dfmin13.loc[i,'Temp'],
                                dfmin14.loc[i,'Temp']]).min():
        tmin2015_to_show.append(tempmin_2015[i])
        tmin2015_date_to_show.append(date_2015_min[i])
print(tmin2015_to_show)
print( tmin2015_date_to_show)


# In[8]:

import numpy as np
get_ipython().magic('matplotlib notebook')
plt.figure(figsize=(10,10))
dates_min=np.array(date_list_min, dtype='datetime64[D]')
dates_max=np.array(date_list_max, dtype='datetime64[D]')
date_2015max=np.array(date_2015_max, dtype='datetime64[D]')
date_2015min=np.array(tmin2015_date_to_show, dtype='datetime64[D]')
plt.plot(dates_min,temp_list_min)
plt.plot(dates_max,temp_list_max)
plt.scatter(date_2015min,tmin2015_to_show,s=5,c='red')


# In[49]: Label the axises and saves the figure as jpg.
plt.xlabel('Dates')
plt.ylabel('Teperature Celcius')
plt.title('Record high and record low temperatures by day of the year over the period 2005-2014')
plt.legend(['Record Low Temperature ','Record High Temperature','Record Low broken law in 2015 '],frameon=False)
plt.fill_between(np.array(date_list_min),temp_list_min,temp_list_max,facecolor='grey',alpha=0.25)
plt.xticks(['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016'])
plt.savefig('Temp_min_max.jpg')


# In[ ]:



