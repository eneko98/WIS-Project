from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'twitter_link', 'instagram_link', 'spotify_link', 'upcoming_events', 'favorite_artists', 'favorite_albums']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_link': forms.URLInput(attrs={'class': 'form-control'}),
            'spotify_link': forms.URLInput(attrs={'class': 'form-control'}),
            'upcoming_events': forms.Textarea(attrs={'class': 'form-control'}),
            'favorite_artists': forms.Textarea(attrs={'class': 'form-control'}),
            'favorite_albums': forms.Textarea(attrs={'class': 'form-control'}),
        }
