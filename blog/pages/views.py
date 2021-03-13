from django.shortcuts import redirect, render
from user.forms import UserProfileForm
from user.models import UserProfile


def index(request):
    form = None
    current_user = None
    if request.user.is_authenticated:
        user_id = request.user.id
        current_user = UserProfile.objects.get(user_id=user_id)
        if request.method == 'POST':
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                current_user.profile_pic = form.cleaned_data['profile_pic']
                current_user.save()
            return redirect('/')
        else:
            form = UserProfileForm()
    return render(request, 'index.html', {'form': UserProfileForm, 'user_profile': current_user})
