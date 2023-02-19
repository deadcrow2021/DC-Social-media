from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Q

from users.models import Profile
from .models import Post
from .forms import CreateUpdatePost
from django.core.cache import cache


def home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(author__user__username=search_query) | Q(title__icontains=search_query))
    else:
        posts = Post.objects.all()

    ordering = ['-date_posted']
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)


def post(request, post_id):
    post_from_cahce = post_id

    if cache.get(post_from_cahce):
        post = cache.get(post_from_cahce)
    else:
        post = get_object_or_404(Post, pk=post_id)
        cache.set(post_from_cahce, post)
            
    context = {'post': post}
    return render(request, 'posts/post.html', context)


@login_required
def create_post(request):
    form = CreateUpdatePost()
    if request.method == 'POST':
        form = CreateUpdatePost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = Profile.objects.get(user=request.user)
            post.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'posts/create_post.html', context)


@login_required
def update_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    form = CreateUpdatePost(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {'post': post, 'form': form}
    return render(request, 'posts/update_post.html', context)


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.POST:
        post.delete()
        return redirect('index')
    context = {'post': post}
    return render(request, 'posts/delete_post.html', context)
