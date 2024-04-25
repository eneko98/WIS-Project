from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile
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
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        profile = None  # It might be a good idea to handle this case, perhaps redirect to a profile creation view.
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)  # Create a new profile if it doesn't exist

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'edit_profile.html', context)

#Event page

# def events(request):
#     events = Event.objects.all()
#     return render(request, 'events.html', {'events': events})

# def get_event_details(request):
#     if request.method == 'GET' and request.is_ajax():
#         event_id = request.GET.get('event_id')
#         event = Event.objects.get(pk=event_id)
#         event_details = {
#             'artist_name': event.artist_name,
#             'location': event.location,
#             'date': event.date.strftime('%B %d, %Y'),
#             'description': event.description,
#             'artist_photo_url': event.artist_photo.url,
#         }
#         return JsonResponse(event_details)
#     else:
#         return JsonResponse({'error': 'Invalid request'})

#new version


def events(request):
    artists = Event.objects.values_list('artist_name', flat=True).distinct()
    locations = Event.objects.values_list('location', flat=True).distinct()
    times = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Applying filters if any
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