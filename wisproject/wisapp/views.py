from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from .models import UserProfile, Event, Artist
from .forms import SignUpForm, UserProfileForm

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def home(request):
    return render(request, 'home.html')

def artists(request):
    all_artists = Artist.objects.prefetch_related('albums', 'events').all()
    return render(request, 'artists.html', {'artists': all_artists})

def artist_detail(request, artist_id):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="a77b2127f86d4ba8b0ced59c2fa57adf", client_secret="f324f47feba24329a38f42420b38bac1"))

    artist = get_object_or_404(Artist, pk=artist_id)
    
    top_tracks_data = []

    top_tracks_data = sp.artist_top_tracks(artist.spotify_id)['tracks'][:4] if artist.spotify_id else [] 

    related_artists_data = sp.artist_related_artists(artist.spotify_id)['artists'][:4] if artist.spotify_id else []

    top_tracks = [
        {
            'name': track['name'],
            'album': track['album']['name'],
            'release_date': track['album']['release_date'],
            'preview_url': track['preview_url']
        } for track in top_tracks_data if track['preview_url']
    ]

    related_artists = [
        {
            'name': artist['name'],
            'image_url': artist['images'][0]['url'] if artist['images'] else None,
            'spotify_album_url': artist['external_urls']['spotify']
        } for artist in related_artists_data
    ]

    return render(request, 'artist_detail.html', {'artist': artist, 'top_tracks': top_tracks, 'related_artists': related_artists})

def events(request):
    artists = Artist.objects.all()
    locations = Event.objects.order_by('location').values_list('location', flat=True).distinct()
    times = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    artistFilter = request.GET.get('artist')
    locationFilter = request.GET.get('location')
    timeFilter = request.GET.get('time')

    events = Event.objects.select_related('artist_name').all()

    if artistFilter:
        events = events.filter(artist__id=artistFilter)
    if locationFilter:
        events = events.filter(location=locationFilter)
    if timeFilter:
        events = events.filter(date__month=int(timeFilter))

    context = {
        'events': events,
        'artists': artists,
        'locations': locations,
        'times': times,
    }
    return render(request, 'events.html', context)

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event_info.html', {'event': event})

def contact(request):
    return render(request, 'contact.html')

def thank_you(request):
    return render(request, 'thank_you.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'log_in.html')

@login_required
def profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'edit_profile.html', context)

@login_required
def add_to_upcoming(request, event_id):
    event = Event.objects.get(id=event_id)
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.upcoming_events.add(event)
    return redirect('events')

@login_required
def remove_from_upcoming(request, event_id):
    event = Event.objects.get(id=event_id)
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.upcoming_events.remove(event)
    return redirect('events')

@login_required
def add_artists_to_favorites(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.favorite_artists.add(artist)
    return JsonResponse({'status': 'success', 'action': 'added', 'artist_id': artist_id})

@login_required
def remove_artists_from_favorites(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile.favorite_artists.remove(artist)
    return JsonResponse({'status': 'success', 'action': 'removed', 'artist_id': artist_id})

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        send_mail(
            'Subscription Confirmation',
            'Thank you for subscribing to our updates!',
            'recordstarantula@gmail.com',
            [email],
            fail_silently=False,
        )
        return HttpResponseRedirect(reverse('thank_you'))
    return render(request, 'contact.html')
