from django.db import models
from realtors.models import Realtor
from .choices import state_choices,bedroom_choices,price_choices

class Listings (models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30, choices=state_choices, blank=True)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField ( choices=price_choices, blank=True)
    bedroom = models.IntegerField(choices=bedroom_choices, blank=True)
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/')
    photo_1 =  models.ImageField(upload_to='photos/', blank=True)
    photo_2 =  models.ImageField(upload_to='photos/', blank=True)
    photo_3 =  models.ImageField(upload_to='photos/', blank=True)
    photo_4 =  models.ImageField(upload_to='photos/', blank=True)
    photo_5 =  models.ImageField(upload_to='photos/', blank=True)
    photo_6 =  models.ImageField(upload_to='photos/', blank=True)
    is_listed = models.BooleanField(default=True)
    list_date = models.DateField(auto_now=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
