from django.db import models
from django.contrib.auth.models import User, AbstractUser

from django.urls import reverse


# Create your models here.

class User(AbstractUser):
    profile_pic = models.ImageField('Profile Picture', null=True, blank=True, 
                                    help_text='Upload a profile picture!')
    bio = models.TextField(max_length=1000, null=True, blank=True,
                           help_text="Tell us a bit more about yourself!")
    date_of_birth = models.DateField()

    def __str__(self):
        return f"@{self.username}"

    def get_absolute_url(self):
        return reverse("blogger-detail", kwargs={"pk": self.pk})
    