from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('아이디어명', max_length=24)
    image = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    content = models.CharField('아이디어 설명', max_length=60)
    interest = models.IntegerField('아이디어 관심도', default=0)
    devtool = models.CharField('예상 개발툴', max_length=24)
    # 생성 시각, 수정 시각
    created_date = models.DateTimeField('작성일', auto_created=True, auto_now_add=True)
    updated_date = models.DateTimeField('수정일', auto_created=True, auto_now=True)

