# Generated by Django 3.0.7 on 2020-07-19 11:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0023_auto_20200708_0736'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Buget',
            new_name='Budget',
        ),
    ]
