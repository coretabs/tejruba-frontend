from rest_framework import viewsets
from rest_framework import Response

from .models import Experience, Tag
from .serializers import ExperienceSerializer, TagSerializer


class ExperiencesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Experience.objects.all()
        serializer = ExperiencesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Experience.objects.all()
        experience = get_object_or_404(queryset, pk=pk)
        serializer = ExperienceSerializer(experience)
        return Response(serializer.data)


class TagViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Tag.objects.all()
        tag = get_object_or_404(queryset, pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data)
