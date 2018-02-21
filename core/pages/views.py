from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *


_homepage='core.pages:home'
_profile='core.accounts:profile'

# Create your views here.
def homepage(request):
	'''Home page. Log-in if posted to, otherwise display homepage.'''
	if request.user.is_authenticated:
		if request.user.is_active:
			return redirect(_profile)
		else:
			logout(request)
			return HttpResponse('You are not allowed to log in.')

	form = f_Login()
	if request.method == 'POST':
		form = f_Login(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect(_profile)
		else:
			form.errors['username'] = ['You did not specify a valid username/password.']

	return render(request, 'core/homepage.html', context=dict(
		sitename='Twisted Hub: home page', form=form
	))


def log_out(request):
	'''Log out and then redirect to homepage.'''
	logout(request)
	return redirect(_homepage)
