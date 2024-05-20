from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    new_password2 = forms.CharField(
        label='New password confirmation',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
