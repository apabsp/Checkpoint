# Generated by Django 5.0.3 on 2024-05-16 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_reviewtext_review_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
