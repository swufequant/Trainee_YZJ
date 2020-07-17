# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:39:52 2020

@author: 8611
"""

from MongoDBReader import MongoDBReader
import os
import csv
import numpy as np
import datetime
import time
import pandas as pd

def QueryUplimitCodeAndDate():
    reader = MongoDBReader()
    reader.login("")
    filename = "all_info.csv"
    

    with open(filename, 'rt') as file:
        reader_ = csv.reader(file)
        # code = [row[0] for row in reader]
        # date_ = [row[1] for row in reader]
        # uplimit_times = [row[2] for row in reader]
        All_Info=[]
        for i, row in enumerate(reader_):
           code, date, uplimit_times = row
           #print (code, date, uplimit_times)
           #if (i>6):
           Info=[]
           if (i<-1):
               break
          
           Info.append(code)
           Info.append(date)
           Info.append(uplimit_times)
           #print(Info)
           date_ = date.split('-')    
           datenum = int(''.join(date_))
           time_info = reader.QueryUplimitInfo(date = datenum, code = code)   
           for idx in time_info.index:
               if time_info.loc[idx, 'uplimit_times'] == int(uplimit_times):
                  

                   upl_time = time_info.loc[idx,"uplimit_time"]
                   brk_time = time_info.loc[idx,"break_time"]
                   #print(upl_time)
                   #print(brk_time)
                   Info.append(upl_time)
                   Info.append(brk_time)
                    #print(Time_Info)
           All_Info.append(Info)
        #print(All_Info)
        
        df = pd.DataFrame(All_Info, columns=["code", "data", "uplimit_times", 
                                                   "uplimit_time", "break_time"])
        outputpath='Time_Info.csv'
        df.to_csv(outputpath,sep=',',index=False,header=True)

                   
     
if __name__ == "__main__":
    QueryUplimitCodeAndDate()
    #UplimitBreak_timeAndUplimit_time()
   