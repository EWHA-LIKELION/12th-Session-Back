from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('create/', PostList.as_view()),
    path('comments/', CommentView.as_view()),
]