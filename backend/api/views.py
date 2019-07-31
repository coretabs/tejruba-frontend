from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from django.contrib.auth import get_user_model

from .models import Tag, Tujruba, Comment, Profile
from .serializer import TagSerializer, TujrubaSerializer, CommentSerializer, ProfileSerializer, UserSerializer #UserLoginSerializer
from rest_framework.generics import ListAPIView

from rest_framework.permissions import AllowAny, IsAuthenticated

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView



# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))



from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



# class UserLoginAPIView(APIView):
# 	#permission_classes = [IsAuthenticated]
# 	permission_classes = [AllowAny]


# 	def post(self, request, *args, **kwargs):
# 		data = request.data
# 		serializer = UserLoginSerializer(data=data)
# 		if serializer.is_valid():
# 			new_data = serializer.data
# 			return Response(new_data, status=HTTP_200_OK)

# 		return  Response(serializer.errors, status=HTTP_400_BAD_REQUEST)





class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer



class TujrubaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Tujruba.objects.all()
    serializer_class = TujrubaSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer






