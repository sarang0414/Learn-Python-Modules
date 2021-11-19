import tablib

data1 = tablib.Dataset()
data1.append(["A",1,'a'])
data1.append(["B",2,'b'])
data1.append(["C",3,'c'])
data1.append(["D",4,'d'])
print(data1)

with open('test.csv','w') as f:
    f.write(data1.csv)

with open('test.xls','wb') as f:
    f.write(data1.xls)
