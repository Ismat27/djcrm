import imp
from re import L
from django import forms
from django.forms import TextInput, NumberInput, Select
from .models import Lead
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()
class ModelLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent'
        )
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'firstname'
            }),

            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'lastname'
            }),

            'age': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'age'
            }),

            'agent': Select(attrs={
                'class': 'form-select',
                
            }),


        }

class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
