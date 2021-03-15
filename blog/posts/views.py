from django.shortcuts import redirect, render
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from user.models import UserProfile
from .models import Post
from django.core.paginator import Paginator


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET['page']
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/posts.html', {'posts': posts, 'page_obj': page_obj})


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
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})
