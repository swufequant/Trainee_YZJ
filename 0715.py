# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:39:52 2020

@author: 8611
"""

from MongoDBReader import MongoDBReader
import os
import csv
import numpy as np

def QueryUplimitCodeAndDate():
    reader = MongoDBReader()
    reader.login("")
    filename = "all_info.csv"

    with open(filename, 'rt') as file:
        reader = csv.reader(file)
        # code = [row[0] for row in reader]
        # date_ = [row[1] for row in reader]
        # uplimit_times = [row[2] for row in reader]
        for i, row in enumerate(reader):
           code, date, uplimit_times = row
           print (code, date, uplimit_times)
           #if (i>6):
           if (i<-1):
               break
       
       
        
  
if __name__ == "__main__":
    QueryUplimitCodeAndDate()
   