from django.shortcuts import render
from django.http import HttpResponseForbidden


# Create your views here.
def AccountFiles(request, pk):
	return HttpResponseForbidden('You are not authorized to view user files.')
