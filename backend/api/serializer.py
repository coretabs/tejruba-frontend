from rest_framework.serializers import CharField, EmailField, ModelSerializer, HyperlinkedModelSerializer
from .models import Tag, Tujruba, Comment, Profile

from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']

        extra_kwargs = {	
            'password': {'write_only': True}
        }

    def create(self, validated_data):
    	first_name = validated_data['first_name']
    	last_name = validated_data['last_name']
    	username = validated_data['username']
    	email = validated_data['email']
    	password = validated_data['password']
    	user_obj = User(

				first_name = first_name,
				last_name = last_name,				
				username = username,
				email = email
    		)
    	user_obj.set_password(password)
    	user_obj.save()
    	return validated_data
        										

# class UserLoginSerializer(ModelSerializer):

# 	username = CharField()
# 	password =  CharField()

#     class Meta:

#         model = User
#         fields = ['username', 'password']





#     def validate(self, data):

#     	return data






class TagSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('title', 'pk')



class TujrubaSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Tujruba
        fields = ('tag',
            'photo',
            'title',
            'description',
            'publish_date',
            'stars',
            'likes',
            'user')





class CommentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('tujruba',
         	'user',
         	'text',
         	'created_date',
         	'likes',
         	'pk')




class ProfileSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('photo',
         	'name',
         	'bio',
         	'job',
         	'age',
         	'country',
         	'facebook',
         	'instagram',
         	'twitter',
         	'personal_website',
         	'user')
