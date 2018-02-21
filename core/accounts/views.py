from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from core.pages.apps import logged_in
from .models import Account


# Create your views here.

@logged_in
def accountPage(request, **kwargs):
	account = get_object_or_404(Account, user=request.user)
	return render(request, 'accounts/account.html', context={
		'account': account,
	})


@logged_in
def Acct_Details(request, id, **kwargs):
	account = get_object_or_404(Account, pk=id)
	return render(request, 'accounts/account.html', context={
		'account': account,
	})
