# Generated by Django 5.0.7 on 2024-07-17 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='수정일')),
                ('created_date', models.DateTimeField(auto_created=True, auto_now_add=True, verbose_name='작성일')),
                ('title', models.CharField(max_length=24, verbose_name='아이디어명')),
                ('image', models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name='이미지')),
                ('content', models.CharField(max_length=60, verbose_name='아이디어 설명')),
                ('interest', models.IntegerField(default=0, verbose_name='가격')),
                ('devtool', models.CharField(max_length=24, verbose_name='아이디어 관심도')),
            ],
        ),
    ]