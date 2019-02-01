import requests
from bs4 import BeautifulSoup

data = requests.get('')

#load data to bs4
soup = BeautifulSoup(data.text, 'html.parser')

#know structure to nav through bs4
data = []
for tr in soup.find_all('tr'):
    #for td in tr.find_all('td'):
    values = [td.text for td in tr.find_all('td')]
    data.append(values) 

print(data)

#get data tagged as special
data = []
for tr in soup.find_all('tr', {'class': 'special'}):
    values = [td.text for td in tr.find_all('td')]
    data.append(values) 

print(data)
 
#get data tagged as special within various tables and div and specific element
data = []
div = soup.find('div', {'class': 'special_table'})
for tr in div.find_all('tr'):
    values = [td.text for td in tr.find_all('td')]
    data.append(values) 
print(data)
