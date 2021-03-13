from django.shortcuts import redirect, render
from user.forms import UserProfileForm
from user.models import UserProfile


def index(request):
    current_user = None
    if request.user.is_authenticated:
        user_id = request.user.id
        current_user = UserProfile.objects.get(user_id=user_id)

    return render(request, 'index.html', {'user_profile': current_user})
