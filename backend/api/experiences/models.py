from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
	title = models.CharField(max_length=15)
	experience = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name="tags")

	def __str__(self):
		return self.title


class Experience(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	publish_date = models.DateTimeField(auto_now_add=True)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	class Meta:
		ordering = ('publish_date', )
    
	def __str__(self):
		return f"{self.title} by {self.user.username}"