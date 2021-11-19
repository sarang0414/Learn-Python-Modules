import tablib

with open('test.csv') as fr:
    csv_data = fr.read()
    data = tablib.Dataset()
    data.append(csv_data)
print(csv_data)
data1 = data.export('xlsx')
with open('new_test.xlsx','wb') as fw:
    fw.write(data1)