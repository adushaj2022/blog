from django.shortcuts import redirect, render
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from user.models import UserProfile
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


@login_required(redirect_field_name='register')
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            user_id = request.user.id
            current_user = UserProfile.objects.get(user_id=user_id)
            post = form.save(commit=False)
            post.creator = current_user
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})
