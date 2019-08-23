from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Experience, Tag
from .serializers import ExperienceSerializer, TagSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()

    def create(self, request):
        # data = request.data
        print(request.data)
        # data['user_id'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.data, error=serializer.errors)

        # print(dir(request))
        # print(request.auth)
        # print(request.data)

    def perform_create(self, serializer):
        serializer.save()

class TagViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)