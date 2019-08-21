from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import ProfileSerializer


class AccountViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileViewSet(viewsets.ViewSet):
    """
    A ViewSet for update or retrieving profile.
    """
    # def retrieve(self ,request, )
    pass


class settingsViewSet(viewsets.ModelViewSet):
    pass