from django import forms
from .models import Page
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'subtitle', 'author', 'content', 'image']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomLoginForm(AuthenticationForm):
    email = forms.EmailField(required=True)