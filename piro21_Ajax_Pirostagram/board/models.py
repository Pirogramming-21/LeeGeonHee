from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Board(models.Model):
    image = models.ImageField(upload_to='board/%Y%m%d', null=True)
    content = models.TextField(max_length=200)
    like = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=timezone.now)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, default=settings.DEFAULT_USER_ID)
    