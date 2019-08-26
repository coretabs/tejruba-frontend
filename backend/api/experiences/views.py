from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, authentication

from .models import Experience, Tag, Comment, Reply
from .serializers import ExperienceSerializer, TagSerializer, CommentSerializer#, ReplySerializer
from .permissions import IsOwnerOrReadOnly


class ExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.data, error=serializer.errors)

    def perform_create(self, serializer):
        serializer.save()


class TagViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)


class CommentList(APIView):
    """
    comments per post list,
    """
    serializer_class =  CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get(self, request, pk=None):
        queryset = Comment.objects.filter(post=pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)


class ReplyList(APIView):
    # serializer_class =  ReplySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get(self, request, pk=None):
        queryset = Reply.objects.filter(post=pk)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)