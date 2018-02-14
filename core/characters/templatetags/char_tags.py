from django.utils.timezone import now
from django import template


register = template.Library()


@register.simple_tag()
def ageInYears(age, joindate):
	'''Takes a character object and returns the age in years'''
	daysPerYear = 365.2422
	if age == str() or not str(age).isnumeric():
		age = daysPerYear * 21
	if joindate == str():
		joindate = now()
	timeSinceJoin = now() - joindate
	return int((age + timeSinceJoin.days) / daysPerYear)
