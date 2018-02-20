from django import forms


class f_Login(forms.Form):
	username = forms.CharField(label='', widget=forms.TextInput(attrs=dict(
		placeholder='username', id='username')
	))
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs=dict(
		placeholder='password', id='password')
	))
