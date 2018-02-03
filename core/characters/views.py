from django.shortcuts import render, get_object_or_404
from .models import Character


# Create your views here.
def charCardByCID(request, cid, **kwargs):
	character = get_object_or_404(Character, pk=cid)
	return render(request, 'characters/char-card.html', context={
		'character': character,
	})

def charCardByName(request, name, **kwargs):
	character = get_object_or_404(Character, name=name)
	return render(request, 'characters/char-card.html', context={
		'character': character,
	})
