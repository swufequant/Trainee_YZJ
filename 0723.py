import pandas as pd
import numpy as np
import os
import csv
from MongoDBReader import MongoDBReader
from datetime import datetime

def GetSubTable():
    reader = MongoDBReader()
    reader.login("")
    dir = "//192.168.0.197/data/temp/info.csv"
    df = pd.read_csv(dir,dtype={"code":str})
    #sub = df.groupby('min_bigorder',as_index = False).mean()
    #df.groupby('min_bigorder', as_index = False)
    df_gp = df.groupby(by="min_bigorder")
    # 证券代码循环
    for min_bigorder, df_sub in df_gp:
        filename='min_bigorder'+'='+str(min_bigorder)+'.'+'csv'
        try:
            f=open(filename,'w')
            if f:
                #清空文件
                f.truncate()
                #写入新文件
                df_sub.to_csv(filename,sep=',',index=False,mode='w',encoding='utf-8')
        except Exception as e:
            print(e)
            

'''
这个文件和之前的统计信息的区别是他包含了最小大单数min_bigorder是0-9的10种情况
现在需要你用pandas包的groupby将原始数据按照 min_bigorder 拆分成10个子表 并依次统计每个子表的以下信息：
1 破板的概率，  上午/下午 破板的概率
2 破板/不破版的平均收益率
3 fake_time 与 uplimit_time的时间差的均值
收益率数据在yield_rate这一列中
'''
def Cal_Break():
    for i in range(9):
        filename = "min_bigorder=str().csv"    
        df = pd.read_csv(filename)
        date = df['date']
        df['break_time'] = pd.to_datetime(df['break_time'])
        df['time'] = pd.to_datetime(df['data'] + ' ' + '14:57:00.000')
        print(df[df["break_time"] > df['time']].count())#
        


if __name__ == "__main__":
    GetSubTable()
    Cal_Break()     

    
