from urllib.request import urlopen
import re

response = urlopen('https://anandology.com/python-practice-book/index.html')
data = str(response.read())
print(data)
var1 = re.findall("http://[\w.]{1,20}",data)
print(var1)