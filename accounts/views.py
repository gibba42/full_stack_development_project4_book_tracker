from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


def register(request):
    """Register a new user account."""

    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('profile')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                "Account created successfully. Welcome to Book Tracker!"
            )
            return redirect('profile')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    """Display the logged-in user's account page."""

    return render(request, 'accounts/profile.html')


def staff_required(user):
    """Return True when the user can access staff-only pages."""

    return user.is_authenticated and user.is_staff


@user_passes_test(staff_required)
def staff_dashboard(request):
    """Display a staff-only dashboard page."""

    return render(request, 'accounts/staff_dashboard.html')