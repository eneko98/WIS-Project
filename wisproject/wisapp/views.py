from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from .models import UserProfile, Event
from .models import Event
from .forms import SignUpForm, UserProfileForm

def home(request):
    return render(request, 'home.html')

def artists(request):
    return render(request, 'artists.html')

def events(request):
    return render(request, 'events.html')

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

def events(request):
    artists = Event.objects.values_list('artist_name', flat=True).distinct()
    locations = Event.objects.values_list('location', flat=True).distinct()
    times = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    artistFilter = request.GET.get('artist')
    locationFilter = request.GET.get('location')
    timeFilter = request.GET.get('time')

    events = Event.objects.all()

    if artistFilter:
        events = events.filter(artist_name=artistFilter)
    if locationFilter:
        events = events.filter(location=locationFilter)
    if timeFilter:
        events = events.filter(date__month=timeFilter) #timeFilter = request.GET.get('time')

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