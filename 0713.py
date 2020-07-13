import os
#提取文件夹中的文件名称至txt
def ListFilesToTxt(dir_,file,wildcard,recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir_)
    for name in files:
        fullname=os.path.join(dir_,name.split(".")[0])
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion)
        else:
            for ext in exts:
                if(name.endswith(ext)):
                    file.write(name.split(".")[0] + "\n")
                    break
def Test():
    dir_="C:/test/test"
    #
    outfile="info.txt"
    wildcard = ".csv"
    with open(outfile,"w") as file:
        print("successful open file:{}".format(outfile))
        #print ("cannot open the file %s for writing" % outfile)
        ListFilesToTxt(dir_,file,wildcard, 1)
        file.close()
        
import csv
from chardet.universaldetector import UniversalDetector

def get_encode_info(file):
    with open(file, 'rb') as f:
        detector = UniversalDetector()
        for line in f.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result['encoding']
def read_file(file):
    with open(file, 'rb') as f:
        return f.read()
def write_file(content, file):
    with open(file, 'wb') as f:
        f.write(content)
def convert_encode2utf8(file, original_encode, des_encode):
    file_content = read_file(file)
    file_decode = file_content.decode(original_encode, 'ignore')
    file_encode = file_decode.encode(des_encode)
    write_file(file_encode, file)


#处理txt文件并转换为csv文件
def txt2csv():
    ##先把所有文件的encoding都转换成utf-8
    encode_info = get_encode_info("info.txt")
    if encode_info != 'utf-8':
        convert_encode2utf8("info.txt", encode_info, 'utf-8')
    csv_file = os.path.splitext("info.txt")[0] + '.csv'
    with open(csv_file, 'w+', newline='', encoding='utf-8') as csvfile:
        
        writer = csv.writer(csvfile, dialect='excel')
        with open("info.txt", 'r', encoding='utf-8') as txtfile:
            for line in txtfile.readlines():
                line_list = line.strip('\n').split('_')
                writer.writerow(line_list)
#分别表示code,datetime,uplimittimme
if __name__ == '__main__':
    Test()
    txt2csv()