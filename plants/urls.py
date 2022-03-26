from . import views
from django.urls import path

app_name = 'plants'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
]