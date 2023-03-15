from django import forms
from .models import Film,Director
from django.core.exceptions import ValidationError

class AddFilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
        widgets = {
            'release_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'day', 
                       'placeholder': 'Select a date',
                       'type': 'date',
                       }),}

def has_numbers(in_string:str):
    return any(char.isdigit() for char in in_string)

class AddDirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

    def clean_first_name(self):
        name:str = self.cleaned_data.get('first_name')
        if has_numbers(name):
            raise ValidationError("Can't include numbers in first name")
        return name 
    
    def clean_last_name(self):
        name:str = self.cleaned_data.get('last_name')
        if has_numbers(name):
            raise ValidationError("Can't include numbers in last name")
        return name 