from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
