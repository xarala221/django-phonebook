from django.shortcuts import render, get_object_or_404
from .forms import UserProfileForm
from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/contacts/")

    return render(request, "accounts/login.html", {"form": form})


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return redirect("/login/")
    else:
        form = SignUpForm()
    return render(request, "accounts/register.html", {"form": form})


def user_profile(request, id):
    user = get_object_or_404(User, id=id)
    return next


def update_user(request, id):
    user = get_object_or_404(User, id=id)
    profile = Profile.objects.filter(user=user)
    form = UserProfileForm()
    if request.method == "POST":
        update_profile_form = UserProfileForm(request.POST, request.FILES)
        bio = request.POST.get('bio')
        picture = request.FILES.get('picture')
        if update_profile_form.is_valid():
            profile.update(
                bio=bio,
                picture=picture
            )

    return render(request, 'accounts/update_profile.html', {'form': form})
