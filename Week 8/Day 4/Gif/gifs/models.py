from django.db import models


    
class Category(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self) -> str:
        return self.name
    
class Gif(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField()
    uploader_name = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add= True)
    Category = models.ManyToManyField(Category, related_name="gifs")
    likes = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.title