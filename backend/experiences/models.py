from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Tag(models.Model):

    title = models.CharField(max_length=150) 

    def __str__(self):

        return self.title        



class Tujruba(models.Model):

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'media/images')
    title = models.CharField(max_length=150) 
    description = models.TextField(max_length=999)
    publish_date = models.DateTimeField(default=timezone.now)
    stars = models.IntegerField()
    likes = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.title


class Comment(models.Model):
    tujruba = models.ForeignKey('Tujruba', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField()

    def __str__(self):

        return self.user.username + ' on ' + self.tujruba.title




