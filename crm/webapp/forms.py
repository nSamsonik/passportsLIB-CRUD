from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# Регистрация/создание пользователя


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Вход пользователей


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# Добавление новых записей


class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'inv_num', 'ser_num', 'place_pass', 'status_pass']

# Обновление данных записей


class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'inv_num', 'ser_num', 'place_pass', 'status_pass']
