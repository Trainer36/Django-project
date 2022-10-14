from django.contrib.auth.models import User
from django.db import models

# create your model here

class UserProfileInfo(models.Model):
    field = models.OneToOneField(User, on_delete=models.CASCADE)
    user = field
    # additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    def __str__(self):
        return self.user.username