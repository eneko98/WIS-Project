from django.contrib import admin
from .models import UserProfile, Event

# Register your models here.

admin.site.register(UserProfile)

admin.site.register(Event)
