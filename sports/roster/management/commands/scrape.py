from django.core.management.base import BaseCommand, CommandError
from roster.models import Player
from bs4 import BeautifulSoup

import urllib2

class Command(BaseCommand):
	args = '<url>'
	help = 'Parses and imports players from Goheels.com'

	def handle(self, *args, **options):
		try:
			print("starting to scrape")

			#Use code below when file to import is on web server :
			response = urllib2.urlopen("http://www.goheels.com/SportSelect.dbml?SPID=12960&SPSID=668154")
			html = response.read()

			#end server version

			#use this code when file is local:
			#with open ("transcript.html", "r") as tempFile:
			#html = tempFile.read();

			#end local version
			#print html;

			soup = BeautifulSoup(html)

			tabledata = soup.find("table", {"id":"roster-table"}) #find the table
			player_names = []
			player_number = []
			player_links = []
			player_position = []

			for link in tabledata.find_all('a'):
				player_links.append(link.get('href'))
				player_names.append(link.get('title'))

			for position in tabledata.find_all("td", {"class":"position"}):
				player_position.append(position.text.strip())

			print player_position
			print player_names
			print player_links

			for player_link, val in enumerate(player_links):
				print (player_link, val, countPlayers)
				response = urllib2.urlopen("http://goheels.com", val)
				html = response.read()
				soup = BeautifulSoup(html)
				print(player_names[countPlayers])
				player_data = Plater.objecs.create(name= player_names[countPlayers])
				player_data.save()
				countPlayers += 1;

		except Player.DoesNotExist:
			raise CommandError("didn't work")

		self.stdout.write("end of scrape.py")