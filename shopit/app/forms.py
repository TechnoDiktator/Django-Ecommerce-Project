from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext , gettext_lazy as _


class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(required=True ,  label = 'Password' , widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(required=True , label = 'Confirm Password' , widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True ,  label = 'Confirm Password' , widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
        labels = {'email': 'Email'}
        widgets = {'username':forms.TextInput(attrs={'class' : 'form-control'})}


class LoginForm(AuthenticationForm):
    username  = UsernameField(widget = forms.TextInput(attrs={'autofocus':True , 'class': 'form-control' }))
    password = forms.CharField(  label=_("Password") , strip= False  ,   widget=forms.TextInput(attrs={'autocomplete': 'current-password' , 'class':'form-control' }))

    
    





