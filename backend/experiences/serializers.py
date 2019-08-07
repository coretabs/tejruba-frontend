from rest_framework import serializers

from .models import Tag, Experience, Comment


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['title', 'content', 'user', 'tags']


class TagSerializer(serializers.ModelSerializer):
     class Meta:
         model = Tag
         fields = ['title', 'pk']



# class TujrubaSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         # model = Tujruba
#         fields = ('tag',
#             'photo',
#             'title',
#             'description',
#             'publish_date',
#             'stars',
#             'likes',
#             'user')





# class CommentSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ('tujruba',
#          	'user',
#          	'text',
#          	'created_date',
#          	'likes',
#          	'pk')
