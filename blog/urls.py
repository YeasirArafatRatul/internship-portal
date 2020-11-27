from django.urls import path, include
from django.conf import settings
from .views import *

app_name = "blog"

urlpatterns = [
    path('/blog-list', PostListView.as_view(),
         name='blog-list'),
]
