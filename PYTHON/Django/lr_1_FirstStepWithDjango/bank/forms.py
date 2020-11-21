from django import forms
 
class User(forms.Form):
    name = forms.CharField()
