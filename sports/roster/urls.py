#apps url roster/urls.py

from django.conf.urls import patterns, url
from roster import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='roster_home'),
	url(r'^player/$', views.playerList, name='roster_player_list'),
	url(r'^player/(?P<pk>\d+)$', views.player, name='roster_player'),
	)