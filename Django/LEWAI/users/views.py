from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    return render(request, 'register.html', {'form': form})


@login_required
def profile_update(request):
    form = ProfileUpdateForm(instance=request.user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully.')
            return redirect('profile')
    return render(request, 'profile_update.html', {'form': form})


@login_required
def custom_logout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('/')
