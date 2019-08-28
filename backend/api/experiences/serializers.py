from rest_framework import serializers
# from rest_framework_recursive.fields import RecursiveField

from . import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('title', )


class ExperienceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True) 
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Experience
        fields = ['pk', 'user', 'user_name', 'title', 'content', 'publish_date', 'tags']


class CommentSerializer(serializers.ModelSerializer):
    # author = 
    # post = serializers.
    class Meta:
        model = models.Comment 
        fields = ('pk', 'text', 'created_date', 'author', 'post')