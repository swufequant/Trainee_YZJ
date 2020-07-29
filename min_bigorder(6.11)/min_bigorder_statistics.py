import pandas as pd
import numpy as np
import os
import csv
#from MongoDBReader import MongoDBReader
from datetime import datetime
'''
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
'''
这个文件和之前的统计信息的区别是他包含了最小大单数min_bigorder是0-9的10种情况
现在需要你用pandas包的groupby将原始数据按照 min_bigorder 拆分成10个子表 并依次统计每个子表的以下信息：
1 破板的概率，  上午/下午 破板的概率
2 破板/不破版的平均收益率
3 fake_time 与 uplimit_time的时间差的均值
收益率数据在yield_rate这一列中
'''

def getFiles(dir, suffix): # 查找根目录，文件后缀 
    res = []
    for root, directory, files in os.walk(dir):  # =>当前根,根下目录,目录下的文件
        for filename in files:
            name, suf = os.path.splitext(filename) # =>文件名,文件后缀
            if suf == suffix:
                res.append(os.path.join(root, filename)) # =>吧一串字符串组合成路径
    return res

'''

def Cal_Break():
    for i in range(9):
        filename = "min_bigorder=str().csv"    
        df = pd.read_csv(filename)
        date = df['date']
        df['break_time'] = pd.to_datetime(df['break_time'])
        df['time'] = pd.to_datetime(df['data'] + ' ' + '14:57:00.000')
        print(df[df["break_time"] > df['time']].count())#
        
'''

#if __name__ == "__main__":
    #GetSubTable()
    #Cal_Break()
amount = []
Count1 =[]
Count2 =[]
Count3 = []
Count4 = []
Count5 = []
Count6 = []
Times =[]
Probability_all =[]
Probability1=[]
Probability2=[]
Rate1=[]
Rate2=[]
Min_bigorder =[]
Time_ave =[]
for file in getFiles("./", '.csv'):
    #全天破板概率
    df = pd.read_csv(file)
    #print (df)
    date = df['date']
    df['break_time'] = pd.to_datetime(df['break_time'])
    df['uplimit_time']=pd.to_datetime(df['uplimit_time'])
    df['time'] = pd.to_datetime(df['date'] + ' ' + '14:57:00.000')
    count1 = df[df["break_time"] > df['time']].count()['code']
    #print (count1)计数假破板次数
    count2 = df[df["break_time"] < df['time']].count()['code']
    #print (count2)计数真破板次数
    min_bigorder = int(df['min_bigorder'].head(1).values)
    #print (min_bigorder)列举大单数
    times = df['date'].count()#计数每一个最小大单数对应的个数
    probability_all = count2 / times #计数破板概率
    
    Count1.append(count1)
    Count2.append(count2)
    Min_bigorder.append(min_bigorder)
    Probability_all.append("%.2f%%"% (probability_all *100))
    Times.append(times)
    
    #上午下午破板概率
    df["timenum"] = df['uplimit_time'].apply(lambda x: x.hour*10000+x.minute*100 + x.second)
    count3 = df[(df["timenum"]<120000) & (df["break_time"] > df['time'])].count()['code']
    #print (count1)计数上午假破板次数
    count4 = df[(df["timenum"]<120000) & (df["break_time"] < df['time'])].count()['code']
    #print (count2)计数上午真破板次数
    count5 = df[(df["timenum"]>120000) & (df["break_time"] > df['time'])].count()['code']
    #print (count1)计数下午假破板次数
    count6 = df[(df["timenum"]>120000) & (df["break_time"] < df['time'])].count()['code']
    #print (count2)计数下午真破板次数
    probability1 = count4 / (count3 + count4) 
    #计数上午破板概率
    probability2 = count6 / (count5 + count6) 
    #计数下午破板概率
    
    #计算平均收益率
    rate1 =df[df["break_time"] > df['time']]['yield_rate'].mean()#假破板平均收益率
    rate2 =df[df["break_time"] < df['time']]['yield_rate'].mean()#真破板平均收益率
    
    #计算时间差均值
    df['fake_time'] = pd.to_datetime(df['fake_time'])
    time_dif = df['fake_time'] - df['uplimit_time']
    time_ave = time_dif.mean()
         
    
    Count3.append(count3)
    Count4.append(count4)
    Count5.append(count5)
    Count6.append(count6)
    Probability1.append("%.2f%%"%(probability1*100))
    Probability2.append("%.2f%%"%(probability2*100))
    Rate1.append("%.2f%%"%(rate1*100))
    Rate2.append("%.2f%%"%(rate2*100))
    Time_ave.append(str(time_ave)[:-3])
    
    
amount.append(Min_bigorder)
amount.append(Times)
amount.append(Count1)
amount.append(Count2)
amount.append(Probability_all)
amount.append(Count3)
amount.append(Count4)
amount.append(Count5)
amount.append(Count6)
amount.append(Probability1)
amount.append(Probability2)
amount.append(Rate1)
amount.append(Rate2)
amount.append(Time_ave)

print (amount)
    
        
     

    
