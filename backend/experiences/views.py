from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from  experiences.models import Experience, Tag
from  experiences.serializers import ExperienceSerializer, TagSerializer


class ExperienceList(APIView):
    """
    List all experiences, or create a new experience.
    """
    def get(self, request, format=None):
        experiences = Experience.objects.all()
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExperienceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExperiencesDetail(APIView):
    """
    Retrieve, update or delete a experience.
    """
    def get_object(self, pk):
        try:
            return Experience.objects.get(pk=pk)
        except Experience.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        experience = self.get_object(pk)
        serializer = ExperienceSerializer(experience)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        experience = self.get_object(pk)
        serializer = ExperienceSerializer(experience, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        experience = self.get_object(pk)
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import viewsets
# from .models import Tag, Tujruba, Comment
# from experiences.api.serializers import TagSerializer, TujrubaSerializer, CommentSerializer
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny, IsAuthenticated



# class TagViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows messages to be viewed or edited.
#     """
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer



# class TujrubaViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows messages to be viewed or edited.
#     """
#     queryset = Tujruba.objects.all()
#     serializer_class = TujrubaSerializer

# class CommentViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows messages to be viewed or edited.
#     """
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


# # Create your views here.
