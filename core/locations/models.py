from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


# Create your models here.
class AbstractLocation(models.Model):
	'''Common values all locations have'''
	parent = models.ForeignKey(
		'self', on_delete=models.PROTECT,
		null=True, related_name='children')
	tier = models.PositiveSmallIntegerField(default=0)
	name = models.CharField(max_length=80, default='Unnamed Location')
	description = models.TextField(max_length=1024 * 6, blank=True)  # Six kB of text for now

	def __str__(self):
		return "{self.id:7,} [T{self.tier}] {self.name}".format(self=self)

	class Meta:
		abstract = True


class Region(AbstractLocation):
	'''Defines a location in a nebulous, large area sense

	Generally, this is something that is too large for even a group to own.
	Tier is a descending value, 0 is the highest tier (should encapsulate
	the entire accessible world), and the lowest is dependent on database
	implementation.
	'''
	peers = models.ManyToManyField(
		'self', through='RegionLink',
		symmetrical=False, related_name='+')


class Place(AbstractLocation):
	'''Defines a location in a specific, small area sense.

	Generally, this is something that can be described as something owned by
	a single person or a group of people. It exists inside of a Region.
	Tier is a descending value, the highest tier (directly connected to a
	Region) is tier 0, and the lowest is dependent on database implementation.
	In practice, this should probably be restricted to 9 tiers deep, and even
	that is a little high.
	'''
	region = models.ForeignKey('Region', on_delete=models.PROTECT, null=True)
	peers = models.ManyToManyField(
		'self', through='PlaceLink',
		symmetrical=False, related_name='+')


class LocationLink(models.Model):
	'''An abstract link between two Locations'''
	locked = models.BooleanField(default=False)

	def decorate_link_add(location_type):
		'''Decorator that generates a function to add a link between two
		locations, then adds that function to the decorated class.
		'''
		def add(loc1, loc2, bidirectional=True):
			'''Link two Locations together.
			This function does the same thing for both PlaceLinks and RegionLinks.
			Specify bidirection=False if you don't want a symmetric link to be added.
			'''
			if loc1.tier == loc2.tier:
				location_type(source=loc1, destination=loc2).save()
				if bidirectional:
					location_type(source=loc2, destination=loc1).save()
			else:
				raise ValidationError(
					_('Location 1 Tier does not match Location 2 Tier (%(tier1)s != %(tier2)s)'),
					params=dict(tier1=loc1.tier, tier2=loc2.tier),
					code='tier_mismatch'
				)
		location_type.add = add
		return location_type

	def __str__(self):
		return "{0.name} ({0.id}) <--> {1.name} ({1.id})".format(self.source, self.destination)

	class Meta():
		unique_together = ('source', 'destination')
		abstract = True


@LocationLink.decorate_link_add
class RegionLink(LocationLink):
	source = models.ForeignKey('Region', on_delete=models.PROTECT,)
	destination = models.ForeignKey('Region', on_delete=models.PROTECT, related_name='link',)


@LocationLink.decorate_link_add
class PlaceLink(LocationLink):
	source = models.ForeignKey('Place', on_delete=models.PROTECT,)
	destination = models.ForeignKey('Place', on_delete=models.PROTECT, related_name='link',)
