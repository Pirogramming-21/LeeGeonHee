# Generated by Django 5.0.7 on 2024-07-20 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_post_create_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Board',
        ),
    ]
