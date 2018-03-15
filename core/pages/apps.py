from django.contrib.auth.decorators import login_required
from django.apps import AppConfig
from functools import partial

logged_in = partial(login_required, redirect_field_name='')


class Config(AppConfig):
    name = 'core.pages'
