from django.utils.timezone import now
from django import template


register = template.Library()


@register.simple_tag()
def ageInYears(character):
	'''Takes a character object and returns the age in years'''
	daysPerYear = 365.2422
	timeSinceJoin = now() - character.joined
	return int((character.age + timeSinceJoin.days) / daysPerYear)
