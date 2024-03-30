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
    context = {
        'user': user,
        'edit_mode': False,  # Assume we're not in edit mode by default
    }

    # Check if the user is an individual or band and fetch the appropriate profile
    if hasattr(user, 'individualprofile'):
        context['profile'] = user.individualprofile
        context['profile_type'] = 'individual'
    elif hasattr(user, 'bandprofile'):
        context['profile'] = user.bandprofile
        context['profile_type'] = 'band'
    else:
        # Indicate that the profile needs to be edited because it doesn't exist
        context['edit_mode'] = True

    # Render the profile page with the context
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    user = request.user
    profile_type = 'individual' if hasattr(user, 'individualprofile') else 'band'
    
    if profile_type == 'individual':
        profile = user.individualprofile if hasattr(user, 'individualprofile') else None
        form = IndividualProfileForm(instance=profile)
    else:
        profile = user.bandprofile if hasattr(user, 'bandprofile') else None
        form = BandProfileForm(instance=profile)

    if request.method == 'POST':
        if profile_type == 'individual':
            form = IndividualProfileForm(request.POST, request.FILES, instance=profile)
        else:
            form = BandProfileForm(request.POST, request.FILES, instance=profile)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    
    return render(request, 'edit_profile.html', {'form': form, 'profile_type': profile_type})
