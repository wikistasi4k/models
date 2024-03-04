from django.urls import path
from . import views
from .views import create_sample_instances

urlpatterns = [
    path('authors/', views.authors_list, name='authors_list'),
    path('authors/<int:pk>/', views.author_details, name='author_details'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<int:pk>/', views.post_details, name='post_details'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-post/', views.add_post, name='add_post'),
    path('create-sample-instances/', create_sample_instances, name='create_sample_instances'),
]