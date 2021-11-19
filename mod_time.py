import os

files = os.listdir('/home/sarang/AMZSYS/Learn Python Basics/Modules')
for file in files:
    print("File Name : {} -- Length : {} -- Modification Date : {}".format(file,os.stat(file).st_size,os.stat(file).st_mtime))
