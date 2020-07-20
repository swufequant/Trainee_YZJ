import os
import pandas as pd
import numpy as np
import time
from MongoDBReader import MongoDBReader
import csv

def Rate_Calculate():
    reader = MongoDBReader()
    reader.login("")
    filename = 'all_info.csv'
    
    with open(filename, 'rt') as file:
        reader_ = csv.reader(file)
        All_Info = []
        for i, row in enumerate(reader_):
            code, date, uplimit_times = row
            Info = []
            #if (i>3):
            if (i<-1):
               break

            Info.append(code)
            Info.append(date)
            Info.append(uplimit_times)
            #print (Info)
    
            date_ = date.split('-')    
            datenum = int(''.join(date_))
            #print (datenum)

            #提取当日日线信息中的close和pre_close数据
            if int(code) < 400000:
                codenum = "SZ" + code
            else:
                codenum = "SH" + code
            rate_info = reader.QueryStockDayLine(date_st = datenum, date_ed = datenum, code = codenum) 
            time_info = reader.QueryUplimitInfo(date = datenum, code = code)   
            for idx in time_info.index:
               if time_info.loc[idx, 'uplimit_times'] == int(uplimit_times):
                    upl_time = time_info.loc[idx,"uplimit_time"]
                    brk_time = time_info.loc[idx,"break_time"]
                    #print(upl_time)
                    #print(brk_time)
                    Info.append(upl_time)
                    Info.append(brk_time)
            for idx in rate_info.index:        
                close = rate_info.loc[idx,"close"]
                pre_close = rate_info.loc[idx,"pre_close"]
                
                #print (type(close))
                #pre___close = pre_close *1.1
                pre__close = round((pre_close * 1.10),2)
                to_rate = close / (pre__close)
                
                #print (rate)
                #print (close)
                #print(pre__close)
                #Info.append(close)
                #Info.append(pre_close)
                #Info.append(pre__close)
                #Info.append(pre___close)
                #Info.append(to_rate)
                #print (Info)
            
            #提取涨停次日信息
                date_nxt_info = reader.QueryStockDayLine(date_st = datenum, date_num = 2, code = codenum)
                close_nxt = date_nxt_info.loc[1,"close"]
                pre_close_nxt = date_nxt_info.loc[1,"pre_close"]
                rate_nxt = close_nxt / pre_close_nxt
                Rate = to_rate * rate_nxt -1
                
                #Info.append(close_nxt)
                #Info.append(pre_close_nxt)
                #Info.append(rate_nxt)
                Info.append(Rate)
                #print (Info)
            All_Info.append(Info)
        #print (All_Info)

        df = pd.DataFrame(All_Info, columns=["code", "data", "uplimit_times", 
                                                   "uplimit_time", "break_time", "Rate"])
        outputpath='Rate_Info.csv'
        df.to_csv(outputpath,sep=',',index=False,header=True)


                   
'''
    #未复权收益率
    df['a'] = df['close'].shift(-1) / df['pre_close'] * 1.1-1
    #复权收益率
    df['b'] = (df['pre_close']*1.1/df['close'])*(df['close'].shift(-1)/df['pre_close'].shift(-1))-1

'''

if __name__ == "__main__":
    Rate_Calculate()