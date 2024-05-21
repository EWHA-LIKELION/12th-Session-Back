from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('create/',PostList.as_view()),
]
# 새로 생성해줘야하는 파일
# url을 분리해주기 위함
# 그 이유가... 뭐더라?
