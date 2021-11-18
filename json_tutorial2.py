import json

f = open('file.json')
data = json.load(f)
print(data)
f.close()


fw = open('new_file.json','w')
json.dump(data,fw,indent=4)
fw.close()
