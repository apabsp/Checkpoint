# Generated by Django 5.0.3 on 2024-04-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='reviewText',
            field=models.TextField(default='minha Review legal!', max_length=10000),
        ),
    ]
