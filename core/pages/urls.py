from django.urls import path
from .views import *

app_name = "pages"
urlpatterns = [
	path("", homepage, name='home'),
	path('logout', log_out, name='logout'),
]
