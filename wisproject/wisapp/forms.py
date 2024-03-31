from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import IndividualProfile, BandProfile

class SignUpForm(UserCreationForm):
    user_type = forms.ChoiceField(
        choices=[('individual', 'Individual'), ('band', 'Band')],
        widget=forms.RadioSelect,
        initial='individual'
    )
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
        fields = ('user_type', 'email', 'username', 'password1', 'password2')
        
class IndividualProfileForm(forms.ModelForm):
    class Meta:
        model = IndividualProfile
        fields = ['profile_picture', 'bio', 'instruments', 'twitter_link', 'instagram_link', 'spotify_link']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'instruments': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_link': forms.URLInput(attrs={'class': 'form-control'}),
            'spotify_link': forms.URLInput(attrs={'class': 'form-control'}),
        }

class BandProfileForm(forms.ModelForm):
    class Meta:
        model = BandProfile
        fields = ['profile_picture', 'bio', 'website', 'twitter_link', 'instagram_link', 'spotify_link']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_link': forms.URLInput(attrs={'class': 'form-control'}),
            'spotify_link': forms.URLInput(attrs={'class': 'form-control'}),
        }
