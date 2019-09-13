from rest_framework import serializers
# from rest_framework_recursive.fields import RecursiveField

from . import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('title', )


class ExperienceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    #tags = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Experience
        fields = ['user', 'title', 'content', 'publish_date', 'tags']


class CommentSerializer(serializers.ModelSerializer):
    # author = 
    # post = serializers.
    class Meta:
        model = models.Comment 
        fields = ('text', 'created_date', 'author', 'post')