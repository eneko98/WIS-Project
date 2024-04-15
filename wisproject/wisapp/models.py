from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    spotify_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    upcoming_events = models.TextField(blank=True)
    favorite_artists = models.TextField(blank=True, help_text="Other bands or singers they like")
    favorite_albums = models.TextField(blank=True, help_text="Other favorite albums")

    def __str__(self):
        return f"{self.user.username}'s profile"

class Events(models.Model):
    artist_photo = models.ImageField(upload_to='artist_photos')
    artist_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.artist_name
