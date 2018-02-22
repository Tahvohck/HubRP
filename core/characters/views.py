from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from core.pages.apps import logged_in
from .models import Character


def getCharacter(name=None, id=None):
	if name:	return get_object_or_404(Character, name=name)
	elif id:	return get_object_or_404(Character, pk=id)
	else:		raise NameError('Must supply name or id to look up character.')


# Create your views here.
def vCharCard(request, name=None, id=None, **kwargs):
	'''View: Find a character and render a character card'''
	character = getCharacter(name, id)
	return render(request, 'characters/char-card.html', context={
		'character': character, 'css': True, 'noCaptions': False,
    })


@logged_in
def vCharCards(request, **kwargs):
	'''View: Get all character cards'''
	characterList = Character.objects.all()
	return render(request, 'characters/card-all.html', context={
		'characters': characterList,
	})


def vCharacter(request, name=None, id=None):
	'''View: Get character detailed info'''
	character = getCharacter(name, id)
	return render(request, 'characters/char-detail.html', context={
		'character': character, 'css': True, 'noCaptions': False,
	})


def vManage(request):
	charList = request.user.characters.all()
	raise NotImplementedError()


def vCreate(request):
	raise NotImplementedError()
