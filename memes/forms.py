from django import forms
from django.forms import ModelForm

from .models import *

class MemeForm(forms.ModelForm):

	class Meta:
		model= Meme
		fields = '__all__'