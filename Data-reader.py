#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas_datareader.data as web
import datetime
 
 
#read ticker symbols from a file to python symbol list
symbol = [AAPL]
with open('C:\python_programs\ST_50.txt') as f:  
    for line in f:
        symbol.append(line.strip())
f.close
 

 
end = datetime.datetime.today()
 
start = datetime.date(end.year-5,1,1)
 
#set path for csv file
path_out = 'c:/python_programs_output/'
 
 

 
i=0
while i<len(symbol):
    try:
        df = web.DataReader(symbol[i], 'yahoo', start, end)
        df.insert(0,'Symbol',symbol[i])
        df = df.drop(['Adj Close'], axis=1)
        if i == 0:
            df.to_csv(path_out+'yahoo_prices_volumes_for_ST_50_to_csv_demo.csv')
            print (i, symbol[i],'has data stored to csv file')
        else:
            df.to_csv(path_out+'yahoo_prices_volumes_for_ST_50_to_csv_demo.csv',mode = 'a',header=False)
            print (i, symbol[i],'has data stored to csv file')
    except:
        print("No information for ticker # and symbol:")
        print (i,symbol[i])
        continue
    i=i+1


# In[ ]:





# In[ ]:




