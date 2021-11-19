from urllib.request import urlopen
from bs4 import BeautifulSoup

html_file = urlopen('https://anandology.com/python-practice-book/index.html')
html_data = html_file.read()
soup = BeautifulSoup(html_data,'lxml')
#print(soup.prettify())

links = soup.find_all('a')
for link in links:
    print(link["href"])


