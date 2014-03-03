# Create your views here.
from roster.models import Player, Team, Coach
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
	context = {'message': 'This is a dynamic message variable!'}
	return render(request, "roster/home.html", context)

def player(request,pk):
	player = get_object_or_404(Player, id=pk)
	return render(request, "roster/player.html", {'player': player})

def playerList(request):
	context = {
		'coaches':Coach.objects.all(),
		'players':Player.objects.all()
	}
	return render(request, "roster/player_list.html", context)

def team(request):
	team = get_object_or_404(Team, id=pk)
	return render(request, "roster/team.html", {'team':team})

def teamList(request):
	team_list = Team.objects.all()
	paginator = Paginator(team_list, 100)
	page = request.GET.get('page')
	try:
		teams=paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, deliver first page.
		teams=paginator.page(1)
	except EmptyPage:
		#i f page is out of range (eg 9000), deliver last page of results.
		teams = paginator.page(paginator.num_pages)

	return render(request, 'roster/team_list.html', {"teams":teams})

def coach(request,pk):
	coach = get_object_or_404(Coach, id=pk)
	return render(request, "roster/coach.html", {"coach":coach})

def coachList(request):
	coach_list = Coach.objects.all()
	paginator = Paginator(coach_list, 100)
	page = request.GET.get('page')
	try:
		coaches=paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, deliver first page.
		coaches=paginator.page(1)
	except EmptyPage:
		#i f page is out of range (eg 9000), deliver last page of results.
		coaches = paginator.page(paginator.num_pages)

	return render(request, 'roster/coach_list.html', {"coaches":coaches})






