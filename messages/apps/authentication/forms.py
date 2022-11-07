from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
)
from django import forms


class UserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control block-form-control",
                "placeholder": "Enter your username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control block-form-control",
                "placeholder": "Enter your password",
            }
        )
    )


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username", "first_name", "last_name")

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control block-form-control",
                "placeholder": "Username",
            }
        )
    )
    first_name = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control inline-form-control",
                "placeholder": "First Name",
            }
        )
    )
    last_name = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control inline-form-control",
                "placeholder": "Last Name",
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control block-form-control",
                "placeholder": "Password",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control block-form-control",
                "placeholder": "Confirm password",
            }
        )
    )
