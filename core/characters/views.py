from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Character


# Create your views here.
def charCard(request, character, **kwargs):
	'''Given a character, calculate their age now, then render a character card'''
	ageNow = (now() - character.joined).days + character.age
	return render(request, 'characters/char-card.html', context={
		'character': character,
		'calcAge': ageNow,
		'css': True, 'noCaptions': False,
	})

def charCardByCID(request, cid, **kwargs):
	'''Get character by CID then pass to `charCard()`'''
	character = get_object_or_404(Character, pk=cid)
	return charCard(request, character, **kwargs)

def charCardByName(request, name, **kwargs):
	'''Get character by name then pass to `charCard()`'''
	character = get_object_or_404(Character, name=name)
	return charCard(request, character, **kwargs)
