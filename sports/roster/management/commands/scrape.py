from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from roster.models import Team, Player

import urllib2
import re



class Command(BaseCommand):
    args = '<url>'
    help = 'Parses ad imports players from GoHeels.com'
    
    def handle (self, *args, **options):
        try:
            print ("trying to scrape")
            
            #use code below when file to import is on web server :
            response = urllib2.urlopen("http://www.goheels.com/SportSelect.dbml?SITE=UNC&DB_OEM_ID=3350&SPID=12960&SPSID=668154")
            html = response.read()
            
            soup = BeautifulSoup(html)
            
            
            tabledata = soup.find("table", {"id": "roster-table"}) #find the proper table
            player_names = []#list to store every player in the table
            player_links = []
            player_position = []
            player_numbers = []
            
            
            print ("starting to scrape")
            
            #Use code below when file ot import is on the web server :
            
            
            
            
            for link in tabledata.find_all('a'):
                player_links.append(link.get('href'))
                player_names.append(link.get('title'))
                
                
            #getting data in tag, .text - just txt inside of node, if you want the tag and no white strip - .strip
            for position in tabledata.find_all("td", {"class" : "position"}):
                player_position.append(position.text.strip())
            
            print player_names
            
            print player_position
                
            print player_links
            for player_link, val in enumerate(player_links):
            
                print(player_link, val, countPlayers)
                response = urllib2.urlopen("http://goheels.com", val)
                html = response.read()
                soup = BeautifulSoup(html)
                print(player_names[countPlayers])
                player_data = Player.objects.create(name= player_names[countPlayers])
                player_data.save()
                countPlayers += 1;
            
            
            
        except Student>doesNotExist:
            raise CommandError('didn\'t work')
        
        self.stdout.write("end of scrape.py")
   