from django.db import models

# Create your models here.

class Player(models.Model):
	name = models.TextField(unique=True)
	dominant_hand = models.TextField(unique=False)
	number = models.IntegerField(unique=False)
	thumbnail = models.TextField(unique=False)
	imgurl = models.TextField(unique=False, null=True)
	position = models.TextField(unique=False)
	height = models.TextField(unique=False)
	weight = models.IntegerField(unique=False)
	year = models.TextField(unique=False)
	hometown = models.TextField(unique=False)
	home_long = models.TextField(unique=False)
	home_lat = models.TextField(unique=False)
	high_school = models.TextField(unique=False)
	batting_avg = models.DecimalField(unique=False, decimal_places=3, max_digits=5)
	gp_gs = models.TextField(unique=False)
	at_bats = models.IntegerField(unique=False)
	runs = models.IntegerField(unique=False)
	hits = models.IntegerField(unique=False)
	doubles = models.IntegerField(unique=False)
	homeruns = models.IntegerField(unique=False)
	rbi = models.IntegerField(unique=False)
	total_bases = models.IntegerField(unique=False)
	slugging = models.DecimalField(unique=False, decimal_places=3, max_digits=5)
	walks = models.IntegerField(unique=False)
	strikeouts = models.IntegerField(unique=False)
	on_base_percentage = models.DecimalField(unique=False, decimal_places=3, max_digits=5)
	assists = models.IntegerField(unique=False)
	errors = models.IntegerField(unique=False)
	story = models.TextField(unique=False)


	class Meta(object):
		verbose_name_plural = "Players"
		ordering = ('name', 'position')

	def __unicode__(self):
		return U'%s %s' %(self.name, self.position)

	def save(self, *args, **kwargs):
		self.name = self.name.upper()

class Team(models.Model):
	name = models.TextField(unique=False)
	gender = models.TextField(unique=False)
	url = models.URLField(unique=False, max_length=400)
	roster_url = models.URLField(unique=False, max_length=400)
	
	class Meta(object):
		verbose_name_plural = "Teams"

	def __unicode__(self):
		return U'%s %s' %(self.name, self.gender)

	def save(self, *args, **kwargs):
		self.name = self.name.upper()

class Coach(models.Model):
	firstname = models.TextField(unique=False)
	lastname = models.TextField(unique=False)
	title = models.TextField(unique=False)
	story = models.TextField(unique=False)
	coaching_age = models.IntegerField(unique=False)

	class Meta(object):
		verbose_name_plural = "Coaches"

	def __unicode__(self):
		return U'%s %s' %(self.firstname, self.lastname)

	def save(self, *args, **kwargs):
		self.name = self.lastname.upper()

