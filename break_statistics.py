#做一下描述性统计  所有样本里破板 不破版的比例是多少，破板/不破版的收益率是多少  上午/下午 破板的概率
import numpy as np 
import pandas as pd
from MongoDBReader import MongoDBReader
import csv
import os
import time
from datetime import datetime
import re

def BreakStatistics():
    reader = MongoDBReader()
    reader.login("")
    filename = "Rate_Info.csv"    
    df = pd.read_csv(filename)
    date = df['data']
    df['break_time'] = pd.to_datetime(df['break_time'])
    #print (type(df['break_time']))
    #dt = re.findall(r'^\w + \s(.*?)$',db)
    #print (df.info())#dt = datetime(2015,4,19,12,20)
    df['time'] = pd.to_datetime(df['data'] + ' ' + '14:57:00.000')
    #print(df.info())
    print(df[df["break_time"] > df['time']].count())#个数为3895
'''    with open(filename, 'rt') as file:
        reader_ = csv.reader(file)
        All_Info = []
        for i, row in enumerate(reader_):

            date = df['data']
            df['break_time'] = pd.to_datetime(df['break_time'])
            #print (type(df['break_time']))
            #dt = re.findall(r'^\w + \s(.*?)$',db)
            #print (df.info())#dt = datetime(2015,4,19,12,20)
            df['time'] = pd.to_datetime(df['data'] + ' ' + '14:57:00.000')
            #print(df.info())
            j=0
            if (i<-1):          
                if df['break_time'].__ge__(df['time']) is False:
                    j = j+1
                break
                print (j)
'''    

    #print(type(dt))

 
    #print(date)
    #print (type(break_time))
   
    #print(diff)  
    
if __name__ == "__main__":
    BreakStatistics()
        
