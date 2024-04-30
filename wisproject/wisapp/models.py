from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100)
    photo = models.URLField()
    genre = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    spotify_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    cover_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    photo = models.URLField(blank=True, null=True)
    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='events', null=True)
    location = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.location
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    spotify_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    upcoming_events = models.ManyToManyField(Event, blank=True)
    favorite_artists = models.ManyToManyField('Artist', related_name='favorited_by')
    favorite_albums = models.TextField(blank=True, help_text="Other favorite albums")

    def __str__(self):
        return f"{self.user.username}'s profile"

