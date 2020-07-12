# Generated by Django 3.0.7 on 2020-07-06 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200706_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='saving',
            name='buget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Buget'),
        ),
        migrations.AddField(
            model_name='saving',
            name='spending',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Spending'),
        ),
    ]