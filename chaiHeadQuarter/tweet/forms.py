from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    # meta class contains all fields which are going to use from the models
    class Meta():
        model = Tweet
        fields = ['text', 'photo']
        # the above fields are being returned when this form is used

# this is inbuilt form of Django
class UserRegistrationForm(UserCreationForm):
    # custom added email field whereas username is the existing field in User model
    email = forms.EmailField
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')