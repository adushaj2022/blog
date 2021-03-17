from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile
from django.shortcuts import get_object_or_404


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


def logout_view(request):
    logout(request)
    return redirect('/')

# show specific users profile page


def profile(request, id):
    user = get_object_or_404(UserProfile, pk=id)
    return render(request, 'users/profile.html', {'user': user})
