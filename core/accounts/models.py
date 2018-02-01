'''Models for the things needed for an account'''
from django.db import models
from django.contrib.auth.models import User
from enum import Enum


# Create your models here.
class Account(models.Model):
	'''Information for a player's account.

	Locally, this means that it defines supporter points, but other things will
	be linked to one of these (From this file for example: IPAddresses and
	Fingerprints, both many-to-one). Also includes the signal function
	definition for	creating a new account when a new user is created.
	'''
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	supporter_points = models.PositiveIntegerField(default=0)

	plugins = []
	class Plugin():
		'''Access hook for account extension.

		- Add template to account view (via `template`)
		'''
		template = ''


	def register_plugin(plug):
		'''Register an `Account.plugin` for use.'''
		if issubclass(plug, Account.Plugin) and plug is not Account.Plugin:
			if plug not in Account.plugins:
				Account.plugins.append(plug)
		else:
			raise TypeError('Cannot register a non-plugin')

	def registerNewAccount(instance, created, **kwargs):
		'''Create a new Account whenever a new user is created.
		NOT REGISTERED HERE.
		'''
		if created:
			Account(user=instance).save()

	def __str__(self):
		return '[{0.id:06}] {1.username}'.format(self, self.user)


class Fingerprint(models.Model):
	'''A semi-unique identifier for an account.'''
	class types(Enum):
		'''Possible choices for `type` field'''
		FPTJS2_FULL = 'FingerprintJS2 Full print'
		FPTJS2_NOGL = 'FingerprintJS2 Partial: No WebGL'
		FPTJS2_NOCANV = 'FingerprintJS2 Partial: No Canvas'

	account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='fingerprints',)
	type = models.CharField(
		max_length=16,
		choices=tuple((x.name, x.value) for x in types)  # This lets us use the enum dynamically
	)
	fingerprint = models.UUIDField()
	last_seen = models.DateTimeField(auto_now=True,)
	first_seen = models.DateTimeField(auto_now_add=True,)

	def __str__(self):
		return "{0.fingerprint} ({0.type})".format(self)


class IPAddress(models.Model):
	'''IP Address associated with an account'''
	account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='IP_addresses',)
	IP = models.GenericIPAddressField(unpack_ipv4=True)
	last_seen = models.DateTimeField(auto_now=True,)
	first_seen = models.DateTimeField(auto_now_add=True,)

	def __str__(self):
		return "[{0.id:04}] {0.IP}".format(self)
