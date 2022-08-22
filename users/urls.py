from django.urls import path
from . import views

urlpatterns = [
    path('profile/id<profile_id>', views.profile, name='profile'),
    path('profile/id<user_id>/edit', views.edit_profile, name='edit-profile'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('subscriptions', views.subscribers_posts, name='subscriptions'),
]
