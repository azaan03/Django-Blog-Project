from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Signup Form (User Registration)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Signupform(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Username"
    )
    
    email = forms.EmailField(
        required=True,
        label="Email Address",
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


    def clean(self):
        """
        Validate that both passwords match.
        """
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match. Please try again.")

        return cleaned_data

# Login Form (User Authentication)
class LoginForm(AuthenticationForm):
    # Username field
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Password field
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
