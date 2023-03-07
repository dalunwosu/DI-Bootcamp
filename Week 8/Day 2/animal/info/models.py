from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=50)

class Animals(models.Model):
    name = models.CharField(max_length=50)
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    image = models.URLField(null = True, blank = True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name