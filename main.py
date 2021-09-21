import requests
from bs4 import BeautifulSoup
import csv

# use requests to go to used bike page and get html content

url = 'https://gobikeit.com/used-bikes/'
response = requests.get(url)

# parse html content to get details strictly related to road bikes -- price, name, size, type

content = BeautifulSoup(response.content, features="html.parser")

# open csv file and write headers
csv_file = open('bike_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['price', 'details', 'link'])

for dl in content.find_all('dl'):
  try:
      descriptors = dl.dd.get_text(strip=True)

      # formats strings 
      descriptors = descriptors.replace('NEW', '')
      descriptors = descriptors.replace('–', '')
      descriptors = descriptors.split('.')
      
      price = descriptors[0]
      price = price.replace('$', '')

      details = ''.join(descriptors[1:])

      link = dl.dt.a.get('href')

      # writes row to csv file for each loop
      csv_writer.writerow([price, details, link])

  except:
    descriptors = None

csv_file.close()

      

    

