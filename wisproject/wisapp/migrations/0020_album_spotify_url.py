# Generated by Django 5.0.3 on 2024-05-05 18:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wisapp", "0019_remove_userprofile_favorite_albums_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="spotify_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
