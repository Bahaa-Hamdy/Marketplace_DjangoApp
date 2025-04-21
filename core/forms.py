from django import forms
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
        username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your username',
        'class' : 'w-full py-4 px-6 rounded-xl  '
    }))
        password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Your Password',
        'class' : 'w-full py-4 px-6 rounded-xl  '
    }))


class SignupForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Passwords do not match!")

        return cleaned_data

    def save(self, commit=True):
        # Override save to hash the password
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user