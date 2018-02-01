from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from .models import Account


# Create your views here.
def Denied(request, **kwargs):
	status = 403
	return render(request, 'accounts/denied.html', status=status, context={
		'request': request,
		'status': status
	})
#	return HttpResponseForbidden('')


def Acct_Details(request, id, **kwargs):
	account = get_object_or_404(Account, pk=id)
	return render(request, 'accounts/account.html', context={
		'account': account,
		'plugins': Account.plugins,
	})
