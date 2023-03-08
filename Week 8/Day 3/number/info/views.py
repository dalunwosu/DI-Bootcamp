from django.shortcuts import render
from .models import numbers

def phonenumber_info(requests, phonenumber):
    info_nu = numbers.objects.get(phone_number = phonenumber)
    context = {'name': info_nu}
    
    return render(requests, 'person.html',context )

def name_info(requests, name: str):
    info_nu = numbers.objects.get(name = name)
    context = {'name': info_nu}
    
    return render(requests, 'person.html',context )