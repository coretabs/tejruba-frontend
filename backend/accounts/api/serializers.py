from rest_framework import serializers, exceptions
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from backend.accounts.models import Profile
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _


from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from django.conf import settings



class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        return user



class LoginSerializer(serializers.Serializer):

    username_or_email = serializers.CharField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})



    def validate(self, data):
        username_or_email = data.get('username_or_email', '')
        password = data.get('password', '')

        user_obj = User.objects.filter(email=data.get("username_or_email")).first() or User.objects.filter(username=data.get("username_or_email")).first()
        if username_or_email and password:

            user = authenticate(username=user_obj.username, password=password)

            if user:
                if user.is_active:
                    data["user"] = user
            else:
                msg = 'Unable to log in with provided credentials.'
                raise exceptions.ValidationError(msg)

        else:
            msg = 'Must include either "email" and "password".'
            raise exceptions.ValidationError(msg)
        return data







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
