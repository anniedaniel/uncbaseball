# Create your views here.
from roster.models import Player
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
	context = {'message': 'This is a dynamic message variable!'}
	return render(request, "roster/home.html", context)

def player(request,pk):
	player = get_object_or_404(Player, id=pk)
	return render(request, "roster/player.html", {'player': player})

def playerList(request):
	player_list = Player.objects.all()
	paginator = Paginator(player_list, 25)
	page = request.GET.get('page')
	try:
		players=paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, deliver first page.
		players=paginator.page(1)
	except EmptyPage:
		#i f page is out of range (eg 9000), deliver last page of results.
		players = paginator.page(paginator.num_pages)

	return render(request, 'roster/player_list.html', {"players":players})
