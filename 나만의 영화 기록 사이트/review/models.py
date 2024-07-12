from django.db import models

# Create your models here.
class Review(models.Model):
    title=models.CharField(max_length=100)
    year=models.CharField(max_length=50)
    genre=models.CharField(max_length=50)
    rating=models.IntegerField() #별점
    content = models.TextField(default='')
    director = models.CharField(max_length=100, default='')
    actors = models.CharField(max_length=300, default='')
    running_time = models.IntegerField(default=0)
    

