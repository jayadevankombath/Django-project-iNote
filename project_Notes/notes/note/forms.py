from django import forms
from django.forms.widgets import Widget
from django.core.validators import RegexValidator
class ValidateFrm(forms.Form):
    email=forms.EmailField()
    fullname=forms.CharField(min_length=5)
    password=forms.CharField(min_length=5,widget=forms.PasswordInput)