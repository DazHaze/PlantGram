from . import views
from django.urls import path

app_name = 'plants'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
]