from django.db import models
from django.contrib.auth.models import User


class TagManager(models.Manager):
	def get_queryset(self):
		pass


class Tag(models.Model):
	title = models.CharField(max_length=15)
	# objects = TagManager()

	def __str__(self):
		return self.title


class Experience(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	publish_date = models.DateTimeField(auto_now_add=True)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.ManyToManyField('Tag', related_name="experience")

	class Meta:
		ordering = ('publish_date', )
    
	def __str__(self):
		return f"{self.title} by {self.user.username}"


class Comment(models.Model):
	text = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True)
	post = models.ForeignKey('Experience', on_delete=models.CASCADE, related_name='comments')

	def __str__(self):
		return self.text


class Reply(models.Model):
	text = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)

	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies', null=True)
	comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies')

	def __str__(self):
		return self.text