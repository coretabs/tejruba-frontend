from django.contrib import admin
from django.contrib.auth.models import User

from .models import Profile, SocialAccount


class SocialAccountInline(admin.TabularInline):
    model = SocialAccount


class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        SocialAccountInline,
    ]


class ProfileInline(admin.TabularInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline, ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)