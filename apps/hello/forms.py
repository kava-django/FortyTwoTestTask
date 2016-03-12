from django.shortcuts import render, redirect
from .models import MyContacts
from django import forms


class MyContactsModelForm(forms.ModelForm):
	class Meta:
		model = MyContacts
        fields = '__all__'

