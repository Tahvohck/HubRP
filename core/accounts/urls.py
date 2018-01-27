from django.http import HttpResponseForbidden
from django.urls import path
from .apps import Config
from .views import AccountFiles


app_name = Config.name
urlpatterns = [
	path('<int:pk>/files/', AccountFiles, name='files',)
]
