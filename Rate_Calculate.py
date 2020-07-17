import os
import pandas as pd
import numpy as np
import time
from MongDBReader import MongoDBReader
import os

def Rate_Calculate():
    reader = MongoDBReader()
    reader.login("")
    filename = 'Time_Info.csv'
    
     with open(filename, 'rt') as file:
        reader_ = csv.reader(file)
   
   
        for i, row in enumerate(reader_):
           code, date, uplimit_times = row


           if (i<-1):
               break
    
           date_ = date.split('-')    
           datenum = int(''.join(date_))
           rate_info = reader.QueryStockDayLine(date = datenum, code = code)   
               for idx in time_info.index:
               if rate_info.loc[idx, 'date'] == datenum:
                  

                   close = rate_info.loc[idx,"clode"]
                   pre_close = time_info.loc[idx,"pre_close"]
                   #print(close)
                   #print(pre_close)
                   

    #未复权收益率
    df['a'] = df['close'].shift(-1) / df['pre_close'] * 1.1-1
    #复权收益率
    df['b'] = (df['pre_close']*1.1/df['close'])*(df['close'].shift(-1)/df['pre_close'].shift(-1))-1



if __name__ = "__main__":
    Rate_Calculate()