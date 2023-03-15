from django import forms
from .models import Customer, Rental, Vehicle

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'name'}),
            'last_name': forms.TextInput(attrs={'class': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'email'}),
            'phone_number':forms.TextInput(attrs= {'class': 'TextInput'}),
            'address': forms.TextInput(attrs={'class': 'TextInput'}),
            'city': forms.TextInput(attrs={'class': 'city'}),
            'country':forms.Select(attrs={'class': 'country'})
        }

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = "__all__"
        widgets = {
            'rental_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'day', 
                       'placeholder': 'Select a date',
                       'type': 'date',
                       }),
                'return_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'day', 
                       'placeholder': 'Select a date',
                       'type': 'date',
                       }),
                      'customer': forms.Select(attrs={'class': 'name'}),
                      'vehicle': forms.Select(attrs={'class': 'name'}),

                    }

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"
        widgets = {
            'type': forms.Select(attrs={'class': 'type'}),
            'real_cost': forms.TextInput(attrs={'class':'number'}),
            'size': forms.Select(attrs={'class': 'size'}),
        }

