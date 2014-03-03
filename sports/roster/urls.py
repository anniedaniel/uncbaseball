#apps url roster/urls.py

from django.conf.urls import patterns, url
from roster import views

urlpatterns = patterns('',
	url(r'^$', 'roster.views.home', name='roster_home'),
	url(r'^team/$', 'roster.views.teamList', name='roster_team_list'),
	url(r'^team/(?P<pk>\d+)$', 'roster.views.team', name='roster_team'),
	url(r'^player/$', 'roster.views.playerList', name='roster_player_list'),
	url(r'^player/(?P<pk>\d+)$', 'roster.views.player', name='roster_player'),
	)

