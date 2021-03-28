from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_profile_pic/', views.add_profile_pic, name='add_profile_pic'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('profile/<int:id>/posts', views.profile_posts, name='profile_posts'),
    path('profiles/', views.all_profiles, name='profiles'),
    path('follow/<int:id>/', views.follow_user, name='follow'),
    path('unfollow/<int:id>/', views.unfollow_user, name='unfollow'),
]
