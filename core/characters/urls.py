from django.urls import path
from .apps import Config
from .views import *


app_name = Config.name
urlpatterns = [
	path('cards',			vCharCards,	name='char-card-index'),
	path('manage',			vManage,	name='manage',),
	path('create',			vCreate,	name='create',),
	# These MUST be second-to-last to ensure correct routing.
	path('card/<int:id>',	vCharCard,	name='char-card'),
	path('card/<str:name>',	vCharCard,	name='char-card'),
	# These MUST be last to ensure correct routing.
	path('<int:id>',		vCharacter,	name='char-detail'),
	path('<str:name>',		vCharacter,	name='char-detail'),
]
