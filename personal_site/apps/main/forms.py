from django import forms

class IPForm(forms.Form):
	ip = forms.CharField(max_length=45, required=True)