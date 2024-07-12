from django.db import models

# Create your models here.
class Review(models.Model):
    GENRE_CHOICES = [
        ('액션', '액션'),
        ('코미디', '코미디'),
        ('드라마', '드라마'),
        ('공포', '공포'),
        ('SF', 'SF'),
        ('로맨스', '로맨스'),
        ('애니메이션', '애니메이션'),
        ('다큐멘터리', '다큐멘터리'),
        ('기타', '기타'),
    ]

    title=models.CharField(max_length=100)
    year=models.CharField(max_length=50)
    genre=models.CharField(max_length=50, choices=GENRE_CHOICES)
    rating=models.IntegerField() #별점
    content = models.TextField(default='')
    director = models.CharField(max_length=100, default='')
    actors = models.CharField(max_length=300, default='')
    running_time = models.IntegerField(default=0)
    

