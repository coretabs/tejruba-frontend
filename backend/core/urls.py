"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# from rest_framework_swagger.views import get_swagger_view
# from accounts.views import UserViewSet, ProfileViewSet
# from experiences.views import TagViewSet, TujrubaViewSet, CommentViewSet



# router = routers.DefaultRouter()
# router.register('users', UserViewSet)
# router.register('tag', TagViewSet)
# router.register('tujruba', TujrubaViewSet)
# router.register('comment', CommentViewSet)
# router.register('profile', ProfileViewSet)






urlpatterns = [

    # http://localhost:8000/
    #path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    # path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('admin/', admin.site.urls),

 

    # path('accounts/', include('allauth.urls')),


    #http://localhost:8000/rest-auth/user/ & login/ & logout/ & password/change/ & password/reset/confirm/
    # path('rest-auth/', include('rest_auth.urls')),


    #http://localhost:8000/rest-auth/registration/  & rest-auth/registration/verify-email/ 
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),

    #http://localhost:8000/test-all/ for test all API 
    # path('test-all/', get_swagger_view(title='API Docs'), name='api_docs')



]


