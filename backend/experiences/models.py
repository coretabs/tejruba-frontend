from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tag(models.Model):
    title = models.CharField(max_length=150) 

    class Meta:
        ordering = ("title", )

    def __str__(self):
        return self.title        


class Experience(models.Model):
    title = models.CharField(max_length=150) 
    content = models.TextField(max_length=999)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to = 'media/images', blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="experiences")
    tags = models.ManyToManyField(Tag, related_name="experiences")
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(max_length=300)
    created = models.DateTimeField(default=timezone.now )
    modified = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return f"{self.id} by {self.user}"