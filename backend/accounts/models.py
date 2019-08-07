from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class SocialAccount(models.Model):
    ACCOUNT_TYPES = (
        ('f', 'Facebook'),
        ('t', 'Twitter'),
        ('g', 'Github'),
        ('o', 'Other')
    )
    account_url = models.URLField(max_length=200, default='', blank=True)
    account_type = models.CharField(choices=ACCOUNT_TYPES, default="o")

    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")


class Profile(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    job = models.CharField(max_length=30, blank=True)
    personal_website = models.URLField(max_length=200, blank=True)
    #photo = models.ImageField(upload_to = 'images', blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()