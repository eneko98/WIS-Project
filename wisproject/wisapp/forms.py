from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class SignUpForm(UserCreationForm):
    bio = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'website', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),

        }
