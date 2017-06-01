from django.forms import ModelForm
from django import forms
from Printapp.models import Model_project#,Printer#Teach_project,
from django.utils import timezone



class StlfileForm(forms.Form):
    stl_file = forms.FileField()

class ModelfileForm(forms.Form):
	model_image= forms.ImageField()
	model_file = forms.FileField()