import requests
from bs4 import BeautifulSoup
from pprint import pprint

# use requests to go to used bike page and get html content

url = 'https://gobikeit.com/used-bikes/'
response = requests.get(url)

# parse html content to get details strictly related to road bikes -- price, name, size, type

html_content = BeautifulSoup(response.content)
gallery_items = html_content.find_all('dl')

parsed_content = []

for dl in gallery_items:
  if dl.dd is not None:
      descriptors = dl.dd.string.split('.')
      price = descriptors[0]

      if '$' in price:
        price = price[price.index('$'):]
      details = ''.join(descriptors[1:])

      link = dl.dt.a.get('href')
      
      
      parsed_content.append({
          'price': price,
          'details': details,
          'link': link
      })

pprint(parsed_content)

      

    

