from django.db import models
from django.urls import reverse


# Create your models here.
class Character(models.Model):
	def get_avatar_name(instance, filename):
		aid = instance.account.id
		basepath = reverse('core.accounts:files', args=[aid])
		return "{0}/avatar_{1}_{2}".format(
			basepath.strip('/'),
			instance.name,
			filename
		)

	account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='characters',)
	avatar = models.ImageField(default='accounts/0/files/avatar_null.png', upload_to=get_avatar_name)
	title = models.CharField(max_length=24, blank=True, default='Citizen',)
	name = models.CharField(max_length=24,)
	biography = models.CharField(max_length=10 * 1024, blank=True, default='',)
	shortDesc = models.CharField(max_length=256, blank=True, default='',)
	race = models.CharField(max_length=24, blank=True, default='Human')
	gender = models.CharField(max_length=8, default='')

	def __str__(self):
		return "{0.title} {0.name}".format(self).strip()

	def __repr__(self):
		return (
			"{0.title} {0.name}\n"
			"{0.gender}{1}{0.race}\n"
			"{0.shortDesc}".format(
				self, "" if self.gender == str() else ' ')
			).strip()


class Stats(models.Model):
	character = models.OneToOneField('Character', on_delete=models.CASCADE, related_name="stats+")
	hitpoints = models.PositiveIntegerField(default=0)
	hitpoints_max = models.PositiveIntegerField(default=0)
	stamina = models.PositiveIntegerField(default=10000)  # Counted in hundreths of a stamina point
	stamina_max = models.PositiveIntegerField(default=10000)  # Counted in hundreths of a stamina point
	attack = models.PositiveIntegerField(default=0)
	defense = models.PositiveIntegerField(default=0)
	mana = models.PositiveIntegerField(default=0)

	money = models.PositiveIntegerField(default=0)
