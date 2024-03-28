from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True)
    instruments = models.CharField(max_length=200, blank=True)
    record_label = models.CharField(max_length=100, blank=True)
    social_media_reach = models.IntegerField(default=0)
    instagram_link = models.URLField(blank=True, null=True)
    spotify_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    upcoming_events = models.TextField(blank=True)
    recent_albums = models.TextField(blank=True)
    years_active = models.CharField(max_length=50, blank=True)
    favorite_artists = models.TextField(blank=True, help_text="Other bands or singers they like")
    favorite_albums = models.TextField(blank=True, help_text="Other favorite albums")

    def __str__(self):
        return self.user.username