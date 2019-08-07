from django.urls import path
from experiences import views

urlpatterns = [
    path('experiences/', views.ExperienceList.as_view()),
    path('experiences/<int:pk>/', views.ExperienceDetail.as_view()),
]