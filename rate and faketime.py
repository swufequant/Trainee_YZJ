import pandas as pd
import numpy as np
import os
import csv
from datetime import datetime
from matplotlib import pyplot
from datetime import timedelta


def getFiles(dir, suffix): # 查找根目录，文件后缀 
    res = []
    for root, directory, files in os.walk(dir):  # =>当前根,根下目录,目录下的文件
        for filename in files:
            name, suf = os.path.splitext(filename) # =>文件名,文件后缀
            if suf == suffix:
                res.append(os.path.join(root, filename)) # =>把一串字符串组合成路径
    return res


for file in getFiles("./", '.csv'):
    #全天破板概率
    df = pd.read_csv(file)
    #print (df)
    df['uplimit_time']=pd.to_datetime(df['uplimit_time'])
    df['fake_time'] = pd.to_datetime(df['fake_time'])
    df['time_dif'] = pd.to_datetime(df['fake_time'] - df['uplimit_time'])
    df['timenum'] = df['time_dif'].apply(lambda x: x.hour*3600+x.minute*60 + x.second + x.microsecond*0.001)
    #print (df['timenum'])
    #print (df['time_dif'])
    print(df['timenum'].corr(df['yield_rate']))