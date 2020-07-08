import pandas as pd
import time
from copy import deepcopy
import os
import string
from MongoDBReader import MongoDBReader
import shutil
import os
 
def load_df(date, code, uplimit_times):
    '''
    读取指定文件
    :param date: 日期 "yyyy-mm-dd"格式 或 datetime.datetime 或 datetime.date 类型
    :param code: 六位证券代码
    :param uplimit_times: 涨停次数 自然数
    :return:
    '''
    dir_ = "C:\test"
    filename = "{}\\{}_2020{}_{}.csv".format(dir_, code, date, uplimit_times)
    if not os.path.exists(filename):
        print("{} not exists".format(filename))
        return pd.DataFrame()
    df = pd.read_csv(filename)
    df["datatime"] = pd.to_datetime(df["datatime"])
    return df, code, uplimit_times


source_path = os.path.abspath('\\\\192.168.0.197\\data\\temp')
target_path = os.path.abspath('C:\test')

if not os.path.exists(target_path):
    os.makedirs(target_path)

if os.path.exists(source_path):
    # root 所指的是当前正在遍历的这个文件夹的本身的地址
    # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
    # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.find('datatime') > 20200101 :
                src_file = os.path.join(root, file)
                shutil.copy(src_file, target_path)
                print(src_file)

print('copy files finished!')

'''
def QueryStockInfo(self, code=None, time_stat=False):
        
        查询指定日期[date_st, date_ed] 之间
        :param date_st:
        :param date_ed:
        :param code:
        :return:
        
        basename = "admin"
        tablename = 'StockInfo'
        time_st = 0.0
        if time_stat:
            time_st = time.time()
        db = self.client.get_database(basename)  # 创建base
        table = db.get_collection(tablename)  # 获取表
        condition = {}
        # 证券代码参数检查
        code_condition = self.CodeConditionGenerator(code)
        if code_condition is not None:
            condition["code"] = code_condition
        # 查询
        cursor = table.find(condition, {"_id": 0})
        df = pd.DataFrame(list(cursor))
        if time_stat:
            print("QueryStockInfo data:{} used time:{:.3f}s".format(len(df), time.time() - time_st))
        return df
'''