# Generated by Django 3.0.7 on 2020-07-08 07:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20200707_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spending',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
