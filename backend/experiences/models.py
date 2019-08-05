from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tag(models.Model):
    title = models.CharField(max_length=150) 

    def __str__(self):
        return self.title        


class Experience(models.Model):
    title = models.CharField(max_length=150) 
    content = models.TextField(max_length=999)
    created = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to = 'media/images')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f"<Experience: {self.title}>"


class Comment(models.Model):
    tujruba = models.ForeignKey(Experience, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField()

    def __str__(self):
        return self.user.username + ' on ' + self.tujruba.title