from django.utils.timezone import now
from django import template


register = template.Library()


@register.filter(is_safe=True)
def getAgeInYears(value):
	'''Takes a character object and returns the age in years'''
	daysPerYear = 365.2422
	timeSinceJoin = now() - value.joined
	return int((value.age + timeSinceJoin.days) / daysPerYear)
