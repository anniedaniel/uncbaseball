from django.contrib import admin
from roster.models import Player, Team

class PlayerAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Player, PlayerAdmin)

class TeamAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    
admin.site.register(Team, TeamAdmin)