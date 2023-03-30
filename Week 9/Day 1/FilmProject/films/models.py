
from django.db import models
from country_list import countries_for_language

countries = countries_for_language("en")

categories_list = [("Action","Action"), ("Adventure","Adventure"), ("Comedy","Comedy"), ("Drama","Drama"), ("Fantasy","Fantasy"), ("Horror","Horror"), ("Musicals","Musicals"), ("Mystery","Mystery"), ("Romance","Romance"), ("Science-Fiction","Science-Fiction"),  ("Sports","Sports"), ("Thriller","Thriller"), ("Western","Western")]
class Country(models.Model):
    name = models.CharField(max_length=5,choices=countries, blank=True, null=True)
    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20, choices=categories_list, blank=True, null=True)
    def __str__(self) -> str:
        return self.name
    
class Director(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)   
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}" 

class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    date_added = models.DateField(auto_now_add=True)
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_created')
    available_in_countries = models.ManyToManyField(Country, related_name='countries_available')
    categories = models.ManyToManyField(Category,related_name='films')
    directors = models.ManyToManyField(Director, related_name='films')

    def __str__(self) -> str:
        director_names = ', '.join([director.__str__() for director in self.directors.all()])
        return f"{self.title}, {director_names}, {self.release_date}"

class Poster(models.Model):
    film = models.OneToOneField(Film, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posters/')
    explanation_img = models.CharField(max_length=100)
