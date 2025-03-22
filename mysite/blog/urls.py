from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # /blog
    path("", views.IndexView.as_view(), name="index"),
    # /blog/post_list
    path("post_list", views.PostListView.as_view(), name="post_list"),
    # /blog/post_create
    path("post_create", views.PostCreateView.as_view(), name="post_create"),
]
