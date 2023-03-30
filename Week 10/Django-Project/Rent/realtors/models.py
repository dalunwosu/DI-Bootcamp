from django.db import models

class Realtor (models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/', blank=True)
    description = models.TextField(blank=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15)
    is_MVP = models.BooleanField(default=False)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
