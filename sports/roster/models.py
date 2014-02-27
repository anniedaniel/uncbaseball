from django.db import models

# Create your models here.

class Player(models.Model):
	name = models.TextField(unique=True)
	number = models.IntegerField(unique=False)
	position = models.TextField(unique=False)
	height = models.IntegerField(unique=False)
	weight = models.IntegerField(unique=False)
	homeworn = models.TextField(unique=False)
	year = models.TextField(unique=False)

	class Meta(object):
		verbose_name_plural = "Players"
		ordering = ('name',)

	def __unicode__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.name = self.name.upper()
		super(Player, self).save(*args, **kwargs)
