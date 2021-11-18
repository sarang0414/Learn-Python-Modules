from urllib.request import urlopen
import re

response = urlopen('https://www.google.com/')
data = response.read()
content = str(data)
print(content)
var1 = re.split("<",content)
var2 = re.split(">",str(var1))
print(var2)


