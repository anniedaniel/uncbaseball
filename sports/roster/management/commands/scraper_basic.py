import urllib2
from bs4 import BeautifulSoup
import re


print ("starting to scrape")

#Use code below when file ot import is on the web server :

response = urllib2.urlopen("http://www.goheels.com/SportSelect.dbml?SITE=UNC&DB_OEM_ID=3350&SPID=12960&SPSID=668154")
html = response.read()

soup = BeautifulSoup(html)


tabledata = soup.find("table", {"id": "roster-table"}) #find the proper table
player_names = []#list to store every player in the table
player_links = []
player_position = []


for link in tabledata.find_all('a'):
    player_links.append(link.get('href'))
    player_names.append(link.get('title'))
    
    
#getting data in tag, .text - just txt inside of node, if you want the tag and no white strip - .strip
for position in tabledata.find_all("td", {"class" : "position"}):
    player_position.append(position.text.strip())

print player_names
    
print player_links

print player_position