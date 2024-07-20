from django.db import models
from django.utils import timezone

# Create your models here.
class Board(models.Model):
    image = models.ImageField(upload_to='board/%Y%m%d', null=True)
    content = models.TextField(max_length=200)
    like = models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now)
    