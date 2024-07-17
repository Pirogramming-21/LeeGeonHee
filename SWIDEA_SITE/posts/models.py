from django.db import models
from developtool.models import devtools
from member.models import Member

# Create your models here.
class Post(models.Model):
    title = models.CharField('아이디어명', max_length=24)
    image = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    content = models.CharField('아이디어 설명', max_length=60)
    interest = models.IntegerField('아이디어 관심도', default=0)
    devtool = models.ForeignKey(devtools, on_delete=models.SET_NULL, verbose_name='예상 개발툴', null=True, blank=True)
    user = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='작성자', null=True)
    created_date = models.DateTimeField('작성일', auto_now_add=True)
    def __str__(self):
        return self.name 

