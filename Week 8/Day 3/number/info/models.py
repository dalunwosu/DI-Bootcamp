from django.db import models

class numbers (models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
