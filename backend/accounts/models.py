from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Profile(models.Model):
    photo = models.ImageField(upload_to = 'images', blank=True)
    name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(default='', blank=True)
    job = models.CharField(max_length=150, default='', blank=True)
    age = models.CharField(max_length=150, default='', blank=True)
    country = models.CharField(max_length=150, default='', blank=True)
    facebook = models.URLField(max_length=200, default='', blank=True)
    instagram = models.URLField(max_length=200, default='', blank=True)
    twitter = models.URLField(max_length=200, default='', blank=True)
    personal_website = models.URLField(max_length=200, default='', blank=True)
    #followed_tag_ids
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.user.username

    def save(self, *args, **kwargs):

        self.name = self.user.first_name + ' ' + self.user.last_name
        super().save(*args, **kwargs)

def create_profile(sender, **kwarg):

    if kwarg['created']:
        user_profile = Profile.objects.create(user=kwarg['instance'])

post_save.connect(create_profile, sender=User)