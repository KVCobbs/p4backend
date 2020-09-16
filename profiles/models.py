from django.db import models
from authentication.models import User


# Create your models here.

class Profile(models.Model):

    class Meta:
        verbose_name_plural = 'profiles'

    image_url = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

