from urllib.request import urlopen

response = urlopen('https://www.google.com/')
data = response.read()
print(data)
url_list = 'https://www.google.com/'.split('/')
print(url_list)
if url_list[-1] == '':
    name = 'index.html'
else:
    name = url_list[-1]

f = open(name,'w')
f.write(str(data))
f.close()