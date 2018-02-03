from django.db import models
from django.urls import reverse


# Create your models here.
class Character(models.Model):
	def get_avatar_name(instance, filename):
		aid = instance.account.id
		return "acct{0}/avatar_{1}_{2}".format(aid, instance.name, filename)

	account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='characters',)
	joined = models.DateTimeField(auto_now_add=True)
	lastOn = models.DateTimeField(auto_now=True)

	avatar = models.ImageField(default='acct0/avatar_null.png', upload_to=get_avatar_name)
	title = models.CharField(max_length=24, blank=True, default='Citizen',)
	name = models.CharField(max_length=24, default='John Doe')
	age = models.PositiveIntegerField(default=7670)  # In days, roughly 21 years
	height = models.PositiveSmallIntegerField(default=170)  # In cm

	sex = models.CharField(max_length=8, default='')
	race = models.CharField(max_length=24, blank=True, default='Human')

	biography = models.CharField(max_length=10 * 1024, blank=True, default='',)
	shortDesc = models.CharField(max_length=256, blank=True, default='A nondescript human specimen.',)

	def __repr__(self):
		return "[{0.id}] {0.title} {0.name}".format(self,).strip()


class Stats(models.Model):
	character = models.OneToOneField('Character', on_delete=models.CASCADE, related_name="stats+")
	hitpoints = models.PositiveIntegerField(default=0)
	hitpointsMax = models.PositiveIntegerField(default=0)
	stamina = models.PositiveIntegerField(default=10000)  # Counted in hundredths of a stamina point
	staminaMax = models.PositiveIntegerField(default=10000)  # Counted in hundredths of a stamina point
	attack = models.PositiveIntegerField(default=0)
	defense = models.PositiveIntegerField(default=0)
	mana = models.PositiveIntegerField(default=0)

	money = models.PositiveIntegerField(default=0)

	carryWeight = models.PositiveIntegerField(default=0)
	carryBulk = models.PositiveIntegerField(default=0)
