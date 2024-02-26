from django.urls import path
from .views import create_sample_instances

urlpatterns = [
    path('create-sample-instances/', create_sample_instances, name='create_sample_instances'),
]