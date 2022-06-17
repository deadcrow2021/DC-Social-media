from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('post/<post_id>', views.post, name='post'),
    path('update/<post_id>', views.update_post, name='update-post'),
    path('delete/<post_id>', views.delete_post, name='delete-post'),
    path('create_post', views.create_post, name='create-post'),
]
