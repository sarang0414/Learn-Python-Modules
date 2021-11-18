from urllib.request import urlopen
import json

response = urlopen('http://httpbin.org/get')
data = response.read()
json_data = json.loads(data)
print(json_data)
new_str = json.dumps(json_data,indent=2)
print(new_str)