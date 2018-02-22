from django.http import HttpResponseForbidden
from django.urls import path
from .apps import Config
from .views import *


app_name = Config.name
urlpatterns = [
	path("", accountPage, name='account',),
]
