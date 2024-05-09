from django.contrib import admin
from .models import UserProfile, Event, Artist, Album, News

# Register your models here.

admin.site.register(UserProfile)

admin.site.register(Event)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(News)