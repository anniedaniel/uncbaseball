from django.contrib import admin
from roster.models import Player

class PlayerAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Player, PlayerAdmin)