from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile, Relationship
from django.shortcuts import get_object_or_404
from posts.models import Post


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user_profile = UserProfile.objects.create(
                user=user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'users/index.html', {'form': form})


@login_required()
def add_profile_pic(request):
    user_id = request.user.id
    current_user = UserProfile.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            current_user.profile_pic = form.cleaned_data['profile_pic']
            current_user.save()
            return redirect('/user/profile/'+str(current_user.id)+'/')
    else:
        form = UserProfileForm()
    return render(request, 'users/add_profile_pic.html', {'form': form})


@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')

# show specific users profile page


def profile(request, id):
    user = get_object_or_404(UserProfile, pk=id)
    posts = Post.objects.all()
    return render(request, 'users/profile.html', {'user': user, 'posts': posts})


def profile_posts(request, id):
    user = get_object_or_404(UserProfile, pk=id)
    posts = Post.objects.filter(creator_id=id)
    return render(request, 'users/posts.html', {'user': user, 'posts': posts})


def all_profiles(request):
    profiles = UserProfile.objects.all()
    current_user = UserProfile.objects.get(user_id=request.user.id)
    does_follows = {}
    for prof in profiles:
        if current_user.does_follow(prof.id):
            does_follows[prof.id] = True
        else:
            does_follows[prof.id] = False
    return render(request, 'users/all_profiles.html', {'profiles': profiles, 'does_follows': does_follows})


@login_required()
def follow_user(request, id):
    current_user = UserProfile.objects.get(user_id=request.user.id)
    user_to_follow = get_object_or_404(UserProfile, pk=id)
    new_relationship = Relationship()
    new_relationship.followee = current_user
    new_relationship.following = user_to_follow
    new_relationship.save()
    return redirect('/user/profiles/')


@login_required()
def unfollow_user(request, id):
    current_user = UserProfile.objects.get(user_id=request.user.id)
    unfollow = Relationship.objects.filter(
        followee_id=current_user.id, following_id=id)
    unfollow.delete()
    return redirect('/user/profiles/')
