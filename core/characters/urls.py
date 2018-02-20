from django.urls import path
from .apps import Config
from .views import *


app_name = Config.name
urlpatterns = [
	path('cards',			vCharCards,	name='char-card-index'),
	path('<int:id>',		vCharacter,	name='char-detail'),
	path('<str:name>',		vCharacter,	name='char-detail'),
	path('card/<int:id>',	vCharCard,	name='char-card'),
	path('card/<str:name>',	vCharCard,	name='char-card'),
]
