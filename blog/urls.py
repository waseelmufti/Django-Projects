from django.urls import path
from . import views
from .views import (
    PostListView,
    UserPostListView,
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-blog"),
    path('blog/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('blog/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('blog/new/', PostCreateView.as_view(), name="blog-create"),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name="blog-update"),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name="blog-delete"),
    path('about/', views.about, name="blog-about"),
]
