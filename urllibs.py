from urllib.request import urlopen


my_url = 'https://www.google.com/'
response = urlopen(my_url)
print(response.headers['Transfer-Encoding'])
content = response.read()
print(content)
