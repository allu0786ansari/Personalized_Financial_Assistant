from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages  # Import messages framework
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .models import UserProfile
from .forms import UserProfileForm


def index(request):
    return render(request, "users/index.html")

def custom_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have successfully logged out.")
    return redirect('index')

def home(request):
    return render(request, "users/home.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')

        try:
            user = User.objects.create_user(username=username, email=email, password=password1,
                                            first_name=first_name, last_name=last_name)
            user.is_active = True  # Deactivate account until it is confirmed
            user.save()

            messages.success(request, "Registration successful! Please Sign In.")
            return redirect('signin')

        except Exception as e:
            messages.error(request, f"Error during registration: {e}")
            return redirect('signup')

    return render(request, "users/signup.html")

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if a user with the provided email exists
        try:
            user = User.objects.get(email=email)
            username = user.username  # Retrieve the username associated with the email
        except User.DoesNotExist:
            messages.error(request, "Bad Credentials!")
            return redirect('homepage')

        # Authenticate using the retrieved username
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "users/homepage.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('signin')
    

    return render(request, "users/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged  out successfully!")
    return redirect('index')

def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'users/password_reset.html')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "No account found with that email address.")
            return render(request, 'users/password_reset.html')

        if user:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Keep user logged in after password change
            messages.success(request, "Your password has been reset successfully.")
            return redirect('signin')  # Redirect to login

    return render(request, 'users/password_reset.html')

@login_required
def homepage(requst):
    return render(requst, 'users/homepage.html')

def help(request):
    return render(request, 'users/help.html')

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'form': form,
        'user_profile': user_profile,
    }
    return render(request, 'users/profile.html', context)
