from django.contrib import admin

from . import models



class TagInline(admin.TabularInline):
    model = models.Tag


class ReplyInline(admin.TabularInline):
    model = models.Reply


class CommentAdmin(admin.ModelAdmin):
    inlines = [
        ReplyInline
    ]


class CommentInline(admin.TabularInline):
    model = models.Comment


class ExperienceAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(models.Tag)
admin.site.register(models.Experience, ExperienceAdmin)
admin.site.register(models.Comment, CommentAdmin)