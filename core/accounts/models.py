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

	def __str__(self):
		return '[{0.id:06}] {1.username}'.format(self, self.user)

	def registerNewAccount(instance, created, **kwargs):
		'''Create a new Account whenever a new user is created.
		NOT REGISTERED HERE.
		'''
		if created:
			Account(user=instance).save()


class Fingerprint(models.Model):
	'''A semi-unique identifier for an account.'''
	class types(Enum):
		'''Possible choices for `type` field'''
		FPTJS2_FULL = 'FingerprintJS2 Full print'
		FPTJS2_NOGL = 'FingerprintJS2 Partial: No WebGL'
		FPTJS2_NOCANV = 'FingerprintJS2 Partial: No Canvas'

	account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
	type = models.CharField(
		max_length=16,
		choices=tuple((x.name, x.value) for x in types)  # This lets us use the enum dynamically
	)
	fingerprint = models.UUIDField()

	def __str__(self):
		return "{0.fingerprint} ({0.type})".format(self)


class IPAddress(models.Model):
	'''IP Address associated with an account'''
	account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
	IP = models.GenericIPAddressField(unpack_ipv4=True)

	def __str__(self):
		return "[{0.id:04}] {0.IP}".format(self)


class Settings(models.Model):
	'''Account-wide settings.'''
	account = models.OneToOneField(Account, on_delete=models.CASCADE)
	b_email_DMs = models.BooleanField(default=False)
	b_show_email = models.BooleanField(default=False)
	b_show_donations = models.BooleanField(default=False)
	b_two_factor_auth = models.BooleanField(default=False)  # TODO: 2FA

	two_factor_auth = models.CharField(max_length=128, default='', blank=True)  # TODO: 2FA
