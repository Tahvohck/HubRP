from django.shortcuts import render
from django.http import HttpResponseForbidden


# Create your views here.
def Denied(request, **kwargs):
	status = 403
	return render(request, 'accounts/denied.html', status=status, context={
		'request': request,
		'status': status
	})
#	return HttpResponseForbidden('')
