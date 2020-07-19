from bs4 import BeautifulSoup	
import requests
import csv

#This program will scrape a table from a wikipedia page and generate a
#.csv file that will be used in Coursera Capstone

wiki = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

source = requests.get(wiki).text

soup = BeautifulSoup(source, 'html5lib')

csv_file = open('toronto_neighborhoods.csv', 'w')
csv_writer = csv.writer(csv_file)
soup = soup.find('tbody')

for row in soup.find_all('tr'):
	row = row.text.split('\n')
	
	postal_code = row[1]
	borough = row[3]
	neighborhood = row[5]
	
	csv_writer.writerow([postal_code, borough, neighborhood])
	
csv_file.close

	
