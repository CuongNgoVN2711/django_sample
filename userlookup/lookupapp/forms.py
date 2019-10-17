from django import forms

class UserLookup(forms.Form):
    name = forms.CharField(label="User's name")