'''Models for the things needed for an account'''
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from enum import Enum


# Create your models here.
class Account(models.Model):
	'''Information for a player's account.

	Locally, this means that it defines supporter points, but other things will
	be linked to one of these (From this file for example: IPAddresses and
	Fingerprints, both many-to-one). Also includes the signal function
	definition for	creating a new account when a new user is created.
	'''
	user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
	supporter_points = models.PositiveIntegerField(default=0)

	def __repr__(self):
		return '[{0.id:05}] {1.username}'.format(self, self.user)

	@receiver(post_save, sender=get_user_model())
	def registerNewAccount(instance, created, **kwargs):
		'''Create a new Account whenever a new user is created.'''
		if created:
			Account(user=instance).save()


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

	def __repr__(self):
		return "{0.fingerprint} ({0.type})".format(self)


class IPAddress(models.Model):
	'''IP Address associated with an account'''
	account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='IP_addresses',)
	IP = models.GenericIPAddressField(unpack_ipv4=True)
	last_seen = models.DateTimeField(auto_now=True,)
	first_seen = models.DateTimeField(auto_now_add=True,)

	def __repr__(self):
		return "[{0.id:04}] {0.IP}".format(self)
