# Generated by Django 5.0.3 on 2024-04-28 20:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wisapp", "0011_artist_remove_event_artist_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="album",
            name="cover_url",
            field=models.URLField(blank=True, null=True),
        ),
    ]
