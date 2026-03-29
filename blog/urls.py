from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('new/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post_update'),
    path('api/posts/', views.PostListAPI.as_view(), name='post_list_api'),
    path('api/posts/<int:pk>/', views.PostDetailAPI.as_view(), name='post_detail_api'),
]
