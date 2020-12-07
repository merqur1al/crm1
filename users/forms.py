from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class AuthUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.fields.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.fields.TextInput(attrs={'placeholder': 'Email'}),
        }

    def __init__(self, *args, **kwargs):
        super(AuthUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})