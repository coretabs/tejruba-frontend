from rest_framework import viewsets
from .models import Profile
from backend.accounts.api.serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
#from rest_framework.permissions import AllowAny, IsAuthenticated





# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

