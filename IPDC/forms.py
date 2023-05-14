from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
class InvestorForm(ModelForm):
	class Meta:
		model = Investor
		fields = '__all__'
		exclude=['user']
class LandForm(ModelForm):
	class Meta:
		model=DomesticRequest
		fields='__all__'
		exclude=['investor']
class MessageForm(ModelForm):
	class Meta:
		model=Message
		fields='__all__'
		exclude=['written_by','privatechat']


