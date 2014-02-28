from django.db import models

# Create your models here.

class Player(models.Model):
	name = models.TextField(unique=True, null=True)
	number = models.IntegerField(unique=False, null=True)
	position = models.TextField(unique=False, null=True)
	height = models.IntegerField(unique=False, null=True)
	weight = models.IntegerField(unique=False, null=True)
	hometown = models.TextField(unique=False, null=True)
	year = models.TextField(unique=False, null=True)

	class Meta(object):
		verbose_name_plural = "Players"
		ordering = ('name', 'position')

	def __unicode__(self):
		return self.name

	# def save(self, *args, **kwargs):
	# 	self.name = self.name.upper()
	# 	super(Player, self).save(*args, **kwargs)
