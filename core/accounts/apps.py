from django.apps import AppConfig
from django.db.models.signals import post_save


class AccountsConfig(AppConfig):
	name = 'core.accounts'

	def ready(self):
		post_save.connect(
			self.get_model('Account').registerNewAccount,
			sender='auth.User'
		)
