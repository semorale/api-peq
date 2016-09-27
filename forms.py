# -*- encoding: utf-8 -*-

#STDLIB imports
from datetime import datetime,date
#Core Django Imports
from django import forms
from django.forms.widgets import *
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
#Third Party apps imports

#Imports local apps
from usuarios.models import UserProfile



class GenerarToken(forms.ModelForm):

	class Meta:
		model = Token
		fields = ['user']