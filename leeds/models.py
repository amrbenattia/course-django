from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# User = get_user_model()

class User(AbstractUser):
    pass

class Leed(models.Model):
    # SOURCE_CHOICES = (
    #     ("Youtube", "Youtube"),
    #     ("Google", "Google"),
    #     ("Newsletter", "Newsletter"),
    # )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.last_name
    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField(blank=True, null=True)

# agent will login to the system. 
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
