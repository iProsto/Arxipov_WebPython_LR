from django import forms

class User(forms.Form):
	login = forms.CharField()
	password = forms.CharField()
