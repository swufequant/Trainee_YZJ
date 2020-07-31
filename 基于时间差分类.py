import pandas as pd
import numpy as np
import os
import csv
from MongoDBReader import MongoDBReader
from datetime import datetime
from matplotlib import pyplot
from datetime import timedelta



reader = MongoDBReader()
reader.login("")
dir = "//192.168.0.197/data/temp/info.csv"
df = pd.read_csv(dir,dtype={"code":str})
df['uplimit_time'] =pd.to_datetime(df['uplimit_time'])
df['fake_time'] = pd.to_datetime(df['fake_time'])
df['time_dif'] = pd.to_datetime(df['fake_time'] - df['uplimit_time'])
timenum = df['time_dif'].apply(lambda x: x.hour*3600+x.minute*60 + x.second + x.microsecond*0.001)
print(time_dif.microsecond)
#print(df)
    
'''
for idx in df:
    if df.loc[idx, 'time_dif'] 
'''
