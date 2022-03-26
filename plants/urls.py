from . import views
from django.urls import path
from .views import AddPostView 

app_name = 'plants'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('?P<slug>[\w-]+/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
]