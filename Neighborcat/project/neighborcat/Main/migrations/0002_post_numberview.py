# Generated by Django 4.1 on 2022-08-17 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='numberview',
            field=models.IntegerField(default=0),
        ),
    ]
