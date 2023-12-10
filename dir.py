import os
import datetime as dt
#os.mkdir('D:/demo')

#current directiry
print("String format",os.getcwd())
print("Byte format",os.getcwdb())
#os.rename('first.txt','first1.txt')
#os.renames("first.txt","D:/demofile1.txt")
print(os.path.getsize("C:\Program Files"))
print("files in current directory:",os.listdir(os.getcwd()))
print("files in current directory:",os.listdir('C:\Program Files'))

#os.rmdir('C:\Pr')
dir_list=os.listdir('C:\Program Files')
if len(dir_list)==0:
    print("directory is empty");

print(os.path.isdir('C:\Program Files'))

print("last access time",os.path.getatime('C:\Program Files'))
print("last modified time",os.path.getmtime('C:\Program Files'))

access_time=dt.datetime.fromtimestamp(os.path.getatime('C:\Program Files'))
modified_time=dt.datetime.fromtimestamp(os.path.getmtime('C:\Program Files'))
print(access_time)
print(modified_time)
