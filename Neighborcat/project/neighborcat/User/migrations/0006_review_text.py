# Generated by Django 4.1 on 2022-08-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]