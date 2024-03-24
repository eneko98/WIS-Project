from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import UserProfile
from .forms import SignUpForm
# Create your views here.

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
            try:
                user = form.save()
                UserProfile.objects.get_or_create(user=user)
                login(request, user)
                return redirect('home')
            except IntegrityError:
                form.add_error(None, "A user with that information already exists.")
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'sign_in.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'sign_in.html')

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile': user_profile})
