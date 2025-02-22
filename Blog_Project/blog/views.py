from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import Signupform, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# ===========================
# Home Page View
# ===========================
def home(request):
    return render(request, "blog/home.html")


# ===========================
# Contact Page View
# ===========================
def contact(request):
    return render(request, "blog/contact.html")


# ===========================
# About Page View
# ===========================
def about(request):
    return render(request, "blog/about.html")


# ===========================
# User Login View
# ===========================

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect("dashboard")  # Redirect to dashboard
            else:
                messages.error(request, "Invalid username or password.")  # Show error message
        else:
            messages.error(request, "Invalid username or password.")  # Form validation failed

    else:
        form = LoginForm()
    
    return render(request, "blog/login.html", {"form": form})



# ===========================
# User Logout View
# ===========================
def user_logout(request):
    logout(request)  # Logs the user out
    messages.success(request, "You have successfully logged out.")
    return redirect("home")  # Redirect to home page


# ===========================
# User Signup View
# ===========================
def signup(request):
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            user = form.save()  # Save user
            messages.success(request, "Your account has been created successfully!")
            return redirect("user_login")  # Redirect to dashboard

    else:
        form = Signupform()

    return render(request, "blog/signup.html", {"form": form})


# ===========================
# Dashboard View (Protected Page)
# ===========================
def dashboard(request):
    return render(request, "blog/dashboard.html")
