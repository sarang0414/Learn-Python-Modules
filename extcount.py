import os

list_fies = os.listdir('/home/sarang/AMZSYS/Learn Python Basics/Modules')
print(list_fies)
lists1 = [x.split('.') for x in list_fies]
print(lists1)
dict1 = {}
for data in lists1:
    if len(data)>1:
        dict1[data[1]] = dict1.get(data[1],0)+1
print(dict1)