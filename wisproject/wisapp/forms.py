from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    bio = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
