# Generated by Django 5.0.3 on 2024-05-28 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_review_liked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
