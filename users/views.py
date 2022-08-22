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
def profile(request, profile_id):
    profile_from_cahce = profile_id
    
    if cache.get(profile_from_cahce):
        profile = cache.get(profile_from_cahce)
    else:
        try:
            profile = Profile.objects.get(pk=profile_id)
            cache.set(profile_from_cahce, profile)
        except Profile.DoesNotExist:
            return HttpResponse('Error')
    return render(request, 'users/profile.html', {'profile': profile})


@login_required
def subscribers_posts(request):
    profile = Profile.objects.get(user=request.user)
    subs = [Profile.objects.get(user=sub) for sub in profile.subscribers.all()]
    posts_list = []
    for sub in subs:
        posts = sub.posts.all()
        for post in posts:
            posts_list.append(post)
    posts_list.sort(key=lambda x: x.date_posted, reverse=True)
    print(posts_list)
    return render(request, 'users/subscriptions.html', {'posts': posts_list})


@login_required
def edit_profile(request, user_id):
    user_obj = User.objects.get(pk=request.user.id)
    prof = Profile.objects.get(pk=user_id)
    form = EditProfile(instance=user_obj)
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile', args=(prof.id,)))
    return render(request, 'users/edit_profile.html', {'user_obj': user_obj, 'form': form})


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