from django.urls import path
from .apps import Config
from .views import *


app_name = Config.name
urlpatterns = [
	path('cards',			charCards,		name='char-card'),
	path('card/<int:cid>',	charCardByCID,	name='char-card'),
	path('card/<str:name>',	charCardByName,	name='char-card'),
]
