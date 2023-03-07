from django.shortcuts import render
from .models import numbers

def phonenumber_info(requests, phonenumber):
    info_nu = numbers.objects.get(phone_number = int(phonenumber))
    context = {'personal_info': info_nu}
    
    return render(requests, 'phonenumber.html',context )

def name_info(requests, name):
    info_nu = numbers.objects.get(name = name)
    context = {'name': info_nu}
    
    return render(requests, 'name.html',context )