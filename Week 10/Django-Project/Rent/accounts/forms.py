from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):

    first_name = forms.CharField(label = 'First Name',widget=forms.TextInput(attrs={'class': 'form-control mb-3',}))
    last_name = forms.CharField(label = 'Last Name',widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mb-3'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))

    class Meta:
        model = User
        fields = ("first_name","last_name","username" ,"email","password1", "password2")
