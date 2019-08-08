from django.urls import path
from experiences import views


app_name = "experiences"

urlpatterns = [
    path('', views.ExperienceList.as_view(), name="experience-list"),
    path('<int:pk>/', views.ExperienceDetail.as_view(), name="experience-detail"),
]