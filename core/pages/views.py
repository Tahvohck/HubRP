from django.contrib.auth import authenticate, login, logout, forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *


# Create your views here.
def homepage(request):
	print(request.user)
	if not request.user.is_anonymous:
		return HttpResponse('You are already logged in!')
	form = f_Login()
	if request.method == 'POST':
		form = f_Login(request.POST)
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('pages:home')
		else:
			form.errors['username'] = ['You did not specify a valid username/password.']
	return render(request, 'core/homepage.html', context=dict(
		sitename='Twisted Hub: home page', form=form
	))


def log_out(request):
	logout(request)
	return redirect('/')
