from django.utils.timezone import datetime
from django import forms


class fNewCharacter(forms.Form):
	name = forms.CharField(min_length=3, max_length=24)

	# Age
	ageInYears = forms.IntegerField(label='Age', min_value=0, max_value=5870000)
	birthMonth = forms.ChoiceField(
		label='Birthday',
		# Comprehension: automatically generate all months
		choices=[(m, datetime(1, m, 1).strftime('%B')) for m in range(1, 13)],
	)
	birthDay = forms.IntegerField(label='', min_value=1, max_value=31, required=False, initial=1)

	height = forms.IntegerField(min_value=1, max_value=32750)  # Max for the data store
	race = forms.CharField(max_length=24)

	short = forms.CharField(max_length=256, required=False, widget=forms.Textarea)
