import pandas as pd
import numpy as np
import os
import csv
from MongoDBReader import MongoDBReader
from datetime import datetime
from matplotlib import pyplot
from datetime import timedelta


def GetSubTable():
    reader = MongoDBReader()
    reader.login("")
    dir = "//192.168.0.197/data/temp/info.csv"
    df = pd.read_csv(dir,dtype={"code":str})
    print((df))
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

if __name__ == "__main__":
    GetSubTable()