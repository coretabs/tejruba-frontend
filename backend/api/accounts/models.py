from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(max_length=200)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)
    job = models.CharField(max_length=50)
    #photo
    #social-accounts