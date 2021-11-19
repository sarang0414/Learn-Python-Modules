import tablib

sheet1 = tablib.Dataset()
sheet1.append(['A',1])
sheet1.append(['B',2])

sheet2 = tablib.Dataset()
sheet2.append(['P',3])
sheet2.append(['Q',4])

book = tablib.Databook([sheet2,sheet2])
with open('book.xlsx','wb') as f:
    f.write(book.xlsx)

# data = tablib.Dataset(headers=['First Name', 'Last Name', 'Age'])
# for i in [('Kenneth', 'Reitz', 22), ('Bessie', 'Monke', 21)]:
#     data.append(i)
# print(data.export('json'))
# print(data.export('csv'))
# print(data.export('xlsx'))
# print(data.export('df'))