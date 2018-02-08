from django.urls import path
from .apps import Config
from .views import *


app_name = Config.name
urlpatterns = [
	path('cards',			vCharCards,			name='char-card-index'),
	path('<int:cid>',		vCharByCID,			name='char-detail'),
	path('<str:name>',		vCharByName,		name='char-detail'),
	path('card/<int:cid>',	vCharCardByCID,		name='char-card'),
	path('card/<str:name>',	vCharCardByName,	name='char-card'),
]
