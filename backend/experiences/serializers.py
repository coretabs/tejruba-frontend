from rest_framework import serializers


from .models import Tag, Experience, Comment


class TagSerializer(serializers.ModelSerializer):
     class Meta:
         model = Tag
         fields = ['id', 'title']


class ExperienceSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name="accounts:UserDetail", read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Experience
        fields = ['id', 'title', 'content', 'created', 'modified', 'user', 'user_id', 'tags']
        read_only_fields = ['created', 'modified', 'user_link', 'user', 'user_id', 'tags']
        

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