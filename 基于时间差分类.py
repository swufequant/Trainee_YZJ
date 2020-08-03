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
df = pd.read_csv(dir, dtype={"code":str})

df['uplimit_time'] =pd.to_datetime(df['uplimit_time'])
df['fake_time'] = pd.to_datetime(df['fake_time'])
#df['time_dif'] = pd.to_datetime(df['fake_time'] - df['uplimit_time'])
time_dif = pd.to_datetime(df['fake_time'] - df['uplimit_time'])
timedifnum = time_dif.apply(lambda x: x.hour*3600+x.minute*60 + x.second + x.microsecond*0.000001)
df['timedifnum'] = timedifnum
#print(df)
   
time = []  # time_dif < 20
'''
time1 = []  # time_dif < 20
time2 = []  # 20 <= time_dif < 50
time3 = []  # 50 <= time_dif < 100
time4 = []  # 100 <= time_dif < 200
time5 = []  # 200 <= time_dif < 500
time6 = []  # 500 <= time_dif < 1000
time7 = []  # 1000 <= time_dif < 2000
time8 = []  # 2000 <= time_dif < 5000
time9 = []  # 5000 <= time_dif < 10000
time10 = []  # 10000 <= time_dif
'''
Time_dif0 = []
Time_dif00 = []
Time_dif1 = []
Time_dif2 = []
Time_dif3 = []
Time_dif4 = []
Time_dif5 = []
Time_dif6 = []
Time_dif7 = []
Time_dif8 = []
Time_dif9 = []
Time_dif10 = []
Rate0 = []
Rate00 = []
Rate1 = []
Rate2 = []
Rate3 = []
Rate4 = []
Rate5 = []
Rate6 = []
Rate7 = []
Rate8 = []
Rate9 = []
Rate10 = []

for idx in df.index:
    time0 = []
    if df.loc[idx, 'timedifnum'] < 0.5:
        rate = df.loc[idx,"yield_rate"]
        dif = df.loc[idx,"timedifnum"]
        Time_dif0.append(dif)
        Rate0.append(rate)
    time0.append(Time_dif0)
    time0.append(Rate0)
time.append(time0)
print(np.mean(Rate0))    

for idx in df.index:
    time00 = []
    if 0.5 <= df.loc[idx, 'timedifnum'] < 1:
        rate = df.loc[idx,"yield_rate"]
        dif = df.loc[idx,"timedifnum"]
        Time_dif00.append(dif)
        Rate00.append(rate)
    time00.append(Time_dif00)
    time00.append(Rate00)
time.append(time00)
print(np.mean(Rate00))  

for idx in df.index:
    time1 = []
    if 1 <= df.loc[idx, 'timedifnum'] < 20:
        rate = df.loc[idx,"yield_rate"]
        dif = df.loc[idx,"timedifnum"]
        Time_dif1.append(dif)
        Rate1.append(rate)
    time1.append(Time_dif1)
    time1.append(Rate1)
time.append(time1)
print(np.mean(Rate1))    

for idx in df.index:
    time2 = []
    if 20 <= df.loc[idx, 'timedifnum'] < 50:
        rate = df.loc[idx,"yield_rate"]
        dif = df.loc[idx,"timedifnum"]
        Time_dif2.append(dif)
        Rate2.append(rate)
    time2.append(Time_dif2)
    time2.append(Rate2)
time.append(time2)
print(np.mean(Rate2))    

for idx in df.index:
    time3 = []
    if 50 <= df.loc[idx, 'timedifnum'] < 100:
        rate = df.loc[idx,"yield_rate"]
        dif = df.loc[idx,"timedifnum"]
        Time_dif3.append(dif)
        Rate3.append(rate)
    time3.append(Time_dif3)
    time3.append(Rate3)
time.append(time3)
print(np.mean(Rate3))    

for idx in df.index:
    time4 = []
    if 100 <= df.loc[idx, 'timedifnum'] < 200:
        rate = df.loc[idx,"yield_rate"]
        dif = df.loc[idx,"timedifnum"]
        Time_dif4.append(dif)
        Rate4.append(rate)
    time4.append(Time_dif4)
    time4.append(Rate4)
time.append(time4)
print(np.mean(Rate4))    

for idx in df.index:
    time1 = []
    if 200 <= df.loc[idx, 'timedifnum'] < 500:
        rate = df.loc[idx,"yield_rate"]
        dif = df.loc[idx,"timedifnum"]
        Time_dif5.append(dif)
        Rate5.append(rate)
    time5.append(Time_dif5)
    time5.append(Rate5)
time.append(time5)
print(np.mean(Rate5))    

for idx in df.index:
    time1 = []
    if 500 <= df.loc[idx, 'timedifnum'] < 1000:
        rate = df.loc[idx,"yield_rate"]
        dif = df.loc[idx,"timedifnum"]
        Time_dif6.append(dif)
        Rate6.append(rate)
    time6.append(Time_dif6)
    time6.append(Rate6)
time.append(time6)
print(np.mean(Rate6))    

for idx in df.index:
    time1 = []
    if 1000 <= df.loc[idx, 'timedifnum'] < 2000:
        rate = df.loc[idx,"yield_rate"]
        dif = df.loc[idx,"timedifnum"]
        Time_dif7.append(dif)
        Rate7.append(rate)
    time7.append(Time_dif7)
    time7.append(Rate7)
time.append(time7)
print(np.mean(Rate7))    

for idx in df.index:
    time1 = []
    if 2000 <= df.loc[idx, 'timedifnum'] < 5000:
        rate = df.loc[idx,"yield_rate"]
        dif = df.loc[idx,"timedifnum"]
        Time_dif8.append(dif)
        Rate8.append(rate)
    time8.append(Time_dif8)
    time8.append(Rate8)
time.append(time8)
print(np.mean(Rate8))    

for idx in df.index:
    time1 = []
    if 5000 <= df.loc[idx, 'timedifnum'] < 10000:
        rate = df.loc[idx,"yield_rate"]
        dif = df.loc[idx,"timedifnum"]
        Time_dif9.append(dif)
        Rate9.append(rate)
    time9.append(Time_dif9)
    time9.append(Rate9)
time.append(time9)
print(np.mean(Rate9))    

for idx in df.index:
    time1 = []
    if 10000 <= df.loc[idx, 'timedifnum'] < 20000:
        rate = df.loc[idx,"yield_rate"]
        dif = df.loc[idx,"timedifnum"]
        Time_dif10.append(dif)
        Rate10.append(rate)
    time10.append(Time_dif10)
    time10.append(Rate10)
time.append(time10)
print(np.mean(Rate10))    


