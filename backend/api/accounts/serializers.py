from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer


class UserSerializer(UserDetailsSerializer):
    company_name = serializers.CharField(source="userprofile.company_name")
    bio = serializers.TextField(source="profile.bio")
    birth_date = serializers.DateField(source="profile.birth_date")
    country = serializers.CharField(source="profile.country")
    job = serializers.CharField(source="profile.job")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
                'company_name', 'bio', 'birth_date', 'country', 'job'
        )

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('userprofile', {})
        company_name = profile_data.get('company_name')
        bio = profile_data.get('bio')
        birth_date = profile_data.get('birth_date')
        country = profile_data.get('country')
        job = profile_data.get('job')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.userprofile
        if profile_data:
            profile.company_name = company_name
            profile.bio = bio
            profile.birth_date = birth_date
            profile.country = country
            profile.job = job
            profile.save()
        return instance