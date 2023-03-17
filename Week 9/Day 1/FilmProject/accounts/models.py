from django.db import models
from django.contrib.auth.models import User
from films.models import Film, Director, Category

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',default='NoImageAvailable.jpg')
    favorite_films = models.ManyToManyField(Film) 
    favorite_directors = models.ManyToManyField(Director)
    favorite_categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return f"{self.user}'s Profile"



