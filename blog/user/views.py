from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import UserProfile


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user_profile = UserProfile.objects.create(user=user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'users/index.html', {'form': form})
