from django.urls import path
from .views import *
from .apps import Config

app_name = Config.name
urlpatterns = [
	path("", homepage, name='home'),
	path('logout', log_out, name='logout'),
]
