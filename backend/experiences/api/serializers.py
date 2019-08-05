# from rest_framework.serializers import HyperlinkedModelSerializer

# from experiences.models import Tag, Tujruba, Comment


# class TagSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ('title', 'pk')



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




