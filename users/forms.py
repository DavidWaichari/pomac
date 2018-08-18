from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    name = forms.CharField(label='First Name', required= True)
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email','name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email','name')
