from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create views.
def login_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('blog:home')
            # Todo log the user in
    else:
        login_form = AuthenticationForm()
    return render(request, 'main/login.html', {"login_form": login_form})


def signup_view(request):
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('blog:home')
    else:
        signup_form = UserCreationForm()
    return render(request, 'main/signup.html', {"signup_form": signup_form})


def logout_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            logout(request)
            return redirect('blog:home')
    else:
        messages.add_message(request, messages.INFO, "Login required!")
        return redirect('accounts:login')

