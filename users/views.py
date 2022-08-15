from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EditProfile
from .models import Profile
from django.core.cache import cache

@login_required
def profile(request, user_id):
    profile_from_cahce = user_id
    
    if cache.get(profile_from_cahce):
        profile = cache.get(profile_from_cahce)
    else:
        try:
            profile = Profile.objects.get(pk=user_id)
            cache.set(profile_from_cahce, profile)
        except Profile.DoesNotExist:
                return HttpResponse('Error')
    return render(request, 'users/profile.html', {'profile': profile})


@login_required
def edit_profile(request, user_id):
    profile = User.objects.get(pk=user_id)
    form = EditProfile(instance=profile)
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile', args=user_id))
    return render(request, 'users/edit_profile.html', {'profile': profile, 'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, 'Your Log In info is not valid')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
        
        
def logout_user(request):
    logout(request)
    messages.success(request, 'You was Logged out')
    return redirect('index')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You was registered')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {
        'form':form
    })