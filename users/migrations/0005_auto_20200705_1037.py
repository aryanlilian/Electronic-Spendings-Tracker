# Generated by Django 3.0.7 on 2020-07-05 10:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_buget_savings_spendings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Savings',
            new_name='Saving',
        ),
        migrations.RenameModel(
            old_name='Spendings',
            new_name='Spending',
        ),
    ]
