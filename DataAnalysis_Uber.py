<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"><html><head><META http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body>
# coding: utf-8

# In[1]:

get_ipython().magic(&#39;pylab inline&#39;)
import pandas
import seaborn


# # Loading Dataset Into Memory

# In[3]:

data = pandas.read_csv(&#39;Desktop/<wbr>Anushka/Uber_data_analytics_<wbr>Python/Uber-dataset.csv&#39;)


# In[7]:

data.tail()


# # Data Preparation

# ## Converting datetime and adding some useful columns

# In[17]:

data[&#39;Date/Time&#39;]= data[&#39;Date/Time&#39;].map(pandas.<wbr>to_datetime)


# In[18]:

data.tail()


# In[19]:

def get_dom(dt): #creating seperate column for day of the month i.e. DOM
    return dt.day

data[&#39;dom&#39;]=data[&#39;Date/Time&#39;].<wbr>map(get_dom) #getting the day of the month


# In[20]:

data.tail()


# In[27]:

def get_weekday(dt): #creating seperate column for weekday
    return dt.weekday()

data[&#39;weekday&#39;] = data[&#39;Date/Time&#39;].map(get_<wbr>weekday)

def get_hour(dt):  #creating seperate column for hour
    return dt.hour

data[&#39;hour&#39;] = data[&#39;Date/Time&#39;].map(get_<wbr>hour)

data.tail()


# # Data Analysis

# ## Analysing the Day of the Month Data (Histogram)

# In[33]:

hist(data.dom, bins=30, rwidth=.8, range=(0.5, 30.5))
xlabel(&#39;Date of the Month&#39;)
ylabel(&#39;Frequency&#39;)
title(&#39;Number of Uber Rides by DOM - April 2014&#39;)


# In[35]:

#for k, rows in data.groupby(&#39;dom&#39;):
 #   print((k, len(rows)))
    
def  count_rows(rows):
    return len(rows)

by_date = data.groupby(&#39;dom&#39;).apply(<wbr>count_rows)
by_date


# In[40]:

bar(range(1,31),(by_date))


# In[42]:

by_date_sorted = by_date.sort_values()
by_date_sorted


# In[45]:

bar(range(1, 31), by_date_sorted)
xticks(range(1,31),by_date_<wbr>sorted.index)
xlabel(&#39;Date of the Month&#39;)
ylabel(&#39;Frequency&#39;)
title(&#39;Number of Uber Rides by DOM - April 2014 (SORTED)&#39;)
(&quot;&quot;)


# ## Analyzing by Hour (Histogram)

# In[48]:

hist(data.hour, bins=24, rwidth=.8, range=(.5, 24))
xlabel(&#39;Hour of the Day&#39;)
ylabel(&#39;Frequency&#39;)
title(&#39;Number of Uber Rides by Hour - April 2014&#39;)



# ## Analyzing by Weekday (Histogram)

# In[59]:

hist(data.weekday, bins=7, range=(-.5,6.5), rwidth=.8)
xticks(range(7), &#39;Mon Tue Wed Thu Fri Sat Sun&#39;.split())
xlabel(&#39;Day of the Week&#39;)
ylabel(&#39;Frequency&#39;)
title(&#39;Number of Uber Rides Per Day - April 2014&#39;)


# ## Analysis of Hour and DOW (CROSS ANALYSIS)

# In[64]:

by_cross=data.groupby(&#39;weekday hour&#39;.split()).apply(count_<wbr>rows).unstack()


# In[65]:

seaborn.heatmap(by_cross)


# ## Analysis by Latitude and Longitude

# In[66]:

hist(data[&#39;Lat&#39;],bins=100, range = (40.5,41))
(&quot;&quot;)


# In[68]:

hist(data[&#39;Lon&#39;],bins=100, range = (-74.1,-73.9))
(&quot;&quot;)


# In[79]:

hist(data[&#39;Lon&#39;],bins=100, range = (-74.1,-73.9), color=&#39;b&#39;, alpha=.5, label=&#39;Longitude&#39;)
grid()
legend(loc=&#39;best&#39;)
twiny()
hist(data[&#39;Lat&#39;],bins=100, range = (40.5,41), color=&#39;r&#39;, alpha=.5, label=&#39;Latitude&#39;)
grid()
legend(loc=&#39;upper left&#39;)
(&quot;&quot;)


# In[80]:

plot(data[&#39;Lat&#39;], &#39;.&#39;, ms=20, color=&#39;green&#39;)
xlim(0,100)


# In[81]:

figure(figsize=(20,20))
plot(data[&#39;Lon&#39;], data[&#39;Lat&#39;],&#39;.&#39;, ms=1, alpha=.5)
xlim(-74.2, -73.7)
ylim(40.7, 41)


# In[ ]:



</body></html>