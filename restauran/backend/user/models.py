from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="profile_pics/default-profile.png", upload_to="profile_pics"
    )
    title = models.CharField(max_length=100, default="...")
    information = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"
