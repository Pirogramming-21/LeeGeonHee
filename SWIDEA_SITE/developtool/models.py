from django.db import models

# Create your models here.
class devtools(models.Model):
    name = models.CharField(max_length=24)
    kind = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    def __str__(self):
        return self.name 