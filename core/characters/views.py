from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Character


# Create your views here.
def currentAge(character):
	'''Get character's time-adjusted age.

	Calculated based on join date and saved age (AKA age at join)'''
	return (now() - character.joined).days + character.age


def vCharCard(request, character, **kwargs):
	'''View: Given a character, calculate their age now, then render a character card'''
	ageNow = currentAge(character)
	return render(request, 'characters/char-card.html', context={
		'character': character,
		'calcAge': ageNow,
		'css': True, 'noCaptions': False,
	})


def vCharCardByCID(request, cid, **kwargs):
	'''View: Get character by CID then pass to `charCard()`'''
	character = get_object_or_404(Character, pk=cid)
	return vCharCard(request, character, **kwargs)


def vCharCardByName(request, name, **kwargs):
	'''View: Get character by name then pass to `charCard()`'''
	character = get_object_or_404(Character, name=name)
	return vCharCard(request, character, **kwargs)


def vCharCards(request, **kwargs):
	'''View: Get all character cards'''
	characterList = Character.objects.all()
	for char in characterList:
		char.ageNow = currentAge(character)

	return render(request, 'characters/card-all.html', context={
		'characters': characterList,
	})


def vCharacterDetail():
	'''View: Get character detailed info'''
	ageNow = currentAge(character)
	return render(request, 'characters/char-detail.html', context={
		'character': character,
		'calcAge': ageNow,
		'noCaptions': False,
	})
	pass
