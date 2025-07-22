from django import forms
from .models import *

class customUserForm(forms.ModelForm):
    class Meta:
        model = customUserModel
        fields = ['username', 'email', 'password', 'userTypes']

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = portfolioModel
        fields = '__all__'
        exclude = ['user', 'created_at']