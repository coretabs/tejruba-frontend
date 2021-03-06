from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

from .import models


class ProfileSerializer(serializers.Serializer):
    bio = serializers.CharField()
    birth_date = serializers.DateField()
    country = serializers.CharField()
    job = serializers.CharField()


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Settings 
        fields = '__all__'


class UserSerializer(UserDetailsSerializer):
    profile = ProfileSerializer()
    settings = SettingsSerializer()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
                'bio', 'birth_date', 'country', 'job'
        )

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', {})
        bio = profile_data.get('bio')
        birth_date = profile_data.get('birth_date')
        country = profile_data.get('country')
        job = profile_data.get('job')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.userprofile
        if profile_data:
            profile.bio = bio
            profile.birth_date = birth_date
            profile.country = country
            profile.job = job
            profile.save()
        return instance