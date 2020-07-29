import pandas as pd
import numpy as np
import os
import csv
from datetime import datetime
from matplotlib import pyplot
from datetime import timedelta
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
                res.append(os.path.join(root, filename)) # =>把一串字符串组合成路径
    return res

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
Mean =[]
Ptp = []
Median = []
Std = []
Coe = []
Min = []
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
    
    #时间差分布统计
    Median.append(time_dif.median())

    Ptp.append(time_dif.ptp())
    Std.append(time_dif.std())
    Coe.append((time_dif.mean())/(time_dif.std()))
    Mean.append(time_ave)
    Min.append(time_dif.min())
    

    #频数直方图绘制
    #time = time_dif.hour*10000+time_dif.minute*100+time_dif.second
    def drawHist(time):
      #创建直方图
      #第一个参数为待绘制的定量数据，不同于定性数据，这里并没有事先进行频数统计
      #第二个参数为划分的区间个数
      #pyplot.hist(time,1000)
      bins_ = [0,20,50,100,200,500,1000,2000,5000,10000,20000]
      time.plot(kind = 'hist', bins = bins_, color = 'steelblue', alpha=0.7, 
                rwidth=0.85, normed = False, label = '直方图')
      pyplot.xlabel('Time Difference')
      pyplot.ylabel('Frequency')
      pyplot.xscale('symlog')    #根据分布频率手动设置x轴的刻度
      #pyplot.xticks([0,20,50,100,300,1000,5000,10000,20000])
      pyplot.title('')
      pyplot.grid(True, linestyle='--', alpha=0.5)
      #pyplot.text( '%.0f' % , ha='center', va= 'bottom',fontsize=11)   
      pyplot.show()
 
    drawHist((df['fake_time'] - df['uplimit_time'])/timedelta(seconds=1))
    
    
                        
    
    
amount.append(Min_bigorder)
amount.append(Times)
amount.append(Count1)#假
amount.append(Count2)#真
amount.append(Probability_all)
amount.append(Count3)#上假
amount.append(Count4)#上真
amount.append(Count5)#下假
amount.append(Count6)#下真
amount.append(Probability1)
amount.append(Probability2)
amount.append(Rate1)
amount.append(Rate2)
amount.append(Time_ave)
amount.append(Mean)
amount.append(Median)
amount.append(Ptp)
amount.append(Std)
amount.append(Coe)
amount.append(Min)
print (amount)

        
     

    
