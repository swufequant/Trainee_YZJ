#做一下描述性统计  所有样本里破板 不破版的比例是多少，破板/不破版的收益率是多少  上午/下午 破板的概率
import numpy as np 
import pandas as pd
from MongoDBReader import MongoDBReader
import csv
import os
import time
import datetime

def BreakStatistics():
    filename = "Rate_Info.csv"
    df = pd.read_csv(filename)

    date = df['data']
    break_time = df['break_time']

    #print(date)
    #print (type(break_time))
    #dtime_st = datetime.datetime.strptime('time_st','%H:%M:%S')
 
    time_st = date + ' ' + '14:57:00'

    diff = time_st - break_time
    #print(diff)
    
    
if __name__ == "__main__":
    BreakStatistics()
        
