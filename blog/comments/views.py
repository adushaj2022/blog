from django.shortcuts import HttpResponse, get_object_or_404, render
from posts.models import Post
from user.models import UserProfile
from .forms import CommentForm
from .models import Comment


def comments(pid):
    return Comment.objects.filter(post_id=pid)


def index(request, id):
    post = get_object_or_404(Post, pk=id)
    user_id = request.user.id
    current_user = UserProfile.objects.get(user_id=user_id)
    form = CommentForm()
    post_comment = comments(id)
    context = {'post': post, 'form': form}
    return render(request, 'comments/index.html', context)
