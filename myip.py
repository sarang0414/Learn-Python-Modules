from urllib.request import urlopen
import json

response = urlopen('http://httpbin.org/get')
data = response.read()
data1 = json.loads(data)
print(data1["origin"])
