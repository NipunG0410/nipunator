from django import forms
from .models import Choice

class Question_form(forms.Form):
    answer=forms.CharField(label='',widget=forms.RadioSelect(choices=[('Yes','Yes'),('No','No')]))