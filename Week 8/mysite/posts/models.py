from django.db import models

class Post(models.Model):

    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50) # varchar
    body = models.TextField()
    
    def __str__(self):
        return self.author + ", " + self.title
    
# One - to - One: models.OneToOneField
class Addition(models.Model):

    image = models.URLField()
    styling = models.CharField(max_length=250)
    post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='addition')

    def __str__(self) -> str:
        return self.post.title

# Many - to - Many: models.ManyToManyField

class Category(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post, related_name='categories')

    def __str__(self) -> str:
        return self.name