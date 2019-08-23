from rest_framework import serializers

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