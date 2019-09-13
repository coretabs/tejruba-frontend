from django.urls import path

from . import views


urlpatterns = [
    path('<int:pk>/', views.CommentList.as_view()),
    path('<int:pk>/replies/', views.ReplyList.as_view()),
    path('<int:pk>/replies/<int:pk2>/', views.ReplyList.as_view()),
]