# Generated by Django 2.2.4 on 2019-11-04 08:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_storys', to=settings.AUTH_USER_MODEL),
        ),
    ]
