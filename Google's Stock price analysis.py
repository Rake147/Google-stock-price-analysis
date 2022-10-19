#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf
import datetime
from datetime import date, timedelta


# In[2]:


today=date.today()


# In[3]:


d1= today.strftime("%Y-%m-%d")


# In[4]:


end_date=d1


# In[5]:


d2= date.today()-timedelta(days=365)


# In[6]:


d2= d2.strftime("%Y-%m-%d")


# In[7]:


start_date=d2


# In[8]:


data=yf.download('GOOG', start=start_date,end=end_date, progress=False)


# In[9]:


data.head()


# In[10]:


data.shape


# In[11]:


data["Date"]=data.index


# In[12]:


data = data[["Date","Open","High","Low","Close","Adj Close","Volume"]]


# In[13]:


data.reset_index(drop=True, inplace=True)
data.head()


# # Candlestick Visualization of Google's stock price

# In[14]:


figure=go.Figure(data=[go.Candlestick(x=data["Date"],open=data["Open"],high=data["High"],low=data["Low"],close=data["Close"])])


# In[15]:


figure.update_layout(title="Google Stock Price Analysis", xaxis_rangeslider_visible=False)
figure.show()


# # Bar Plot is a handy tool to Visualize stocks
# 

# In[16]:


figure =px.bar(data,x='Date',y='Close')
figure.show()


# # Stock analysis with rangeslider

# In[17]:


figure=px.line(data,x='Date',y='Close', title='Stock market analysis with rangeslider')
figure.update_xaxes(rangeslider_visible=True)
figure.show()


# # Time period selectors 

# In[22]:


figure=px.line(data,x='Date',y='Close', title='Stock market analysis with Time Period Selectors')
figure.update_xaxes(
    rangeselector=dict(
    buttons=list([
        dict(count=1,label='1m',step='month',stepmode='backward'),
        dict(count=6,label='6m',step='month',stepmode='backward'),
        dict(count=3,label='3m',step='month',stepmode='backward'),
        dict(count=1,label='1y',step='year',stepmode='backward'),
        dict(step="all")
    ])
    )
)
figure.show()


# # Stock Analysis by removing weekend gaps

# In[23]:


figure=px.scatter(data, x='Date', y='Close', range_x=['2021-10-20', '2022-10-18'],
                 title="Stock market analysis by hiding weekend gaps")
figure.update_xaxes(
    rangebreaks=[
        dict(bounds=['sat','sun'])
    ]
)
figure.show()


# In[ ]:




