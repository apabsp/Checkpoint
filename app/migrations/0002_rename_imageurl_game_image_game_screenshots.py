# Generated by Django 5.0.3 on 2024-04-05 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='imageUrl',
            new_name='image',
        ),
        migrations.AddField(
            model_name='game',
            name='screenshots',
            field=models.JSONField(default=dict),
        ),
    ]
