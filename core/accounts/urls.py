from django.http import HttpResponseForbidden
from django.urls import path
from .apps import Config
from .views import Denied, Acct_Details


app_name = Config.name
urlpatterns = [
	path("", Denied, name='account',),
	path('<int:id>/', Acct_Details, name='account',),
	path('<int:pk>/files/', Denied, name='files',),
]
