# Generated by Django 5.0.3 on 2024-04-30 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wisapp', '0017_rename_artist_name_artist_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_photo',
            new_name='photo',
        ),
    ]
