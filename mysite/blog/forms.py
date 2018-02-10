from django import forms
from django.forms import CharField, Form, FileField
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from blog.models import Equipamentos
from django.core.validators import RegexValidator



class EquipamentosForm(Form):
	codigo_equipamento = forms.CharField(max_length=200)
	marca_equipamento  = forms.CharField(max_length=200)
	modelo_equipamento = forms.CharField(max_length=200)
	nome_equipamento   = forms.CharField(max_length=200)
	foto_equipamento   = forms.FileField(required=False)
