from django.urls import path
from .apps import Config
from .views import *


app_name = Config.name
urlpatterns = [
	path('cards',			vCharCards,			name='char-card-index'),
	path('card/<int:cid>',	vCharCardByCID,		name='char-card'),
	path('card/<str:name>',	vCharCardByName,	name='char-card'),
	path('card/<int:cid>',	vCharCardByName,	name='char-detail'),
	path('card/<str:name>',	vCharCardByName,	name='char-detail'),
]
