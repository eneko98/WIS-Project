from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import IndividualProfile, BandProfile
from .forms import SignUpForm, IndividualProfileForm, BandProfileForm

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
        profile = IndividualProfile.objects.get(user=user)
        profile_type = 'individual'
    except IndividualProfile.DoesNotExist:
        profile = BandProfile.objects.get(user=user)
        profile_type = 'band'
    context = {
        'profile': profile,
        'profile_type': profile_type,
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    # Check if the user has an individual profile
    try:
        profile = IndividualProfile.objects.get(user=request.user)
        profile_form = IndividualProfileForm
    except IndividualProfile.DoesNotExist:
        # If not, it must be a band profile
        profile = BandProfile.objects.get(user=request.user)
        profile_form = BandProfileForm

    if request.method == 'POST':
        form = profile_form(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = profile_form(instance=profile)

    context = {'form': form, 'profile': profile}
    return render(request, 'edit_profile.html', context)
