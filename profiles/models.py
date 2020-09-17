from django.db import models
from authentication.models import User


# Create your models here.

class Profile(models.Model):
    class Meta:
        verbose_name_plural = 'profiles'

    # I thought about changing this more to me a profile page. And then the user will have
    # The line image_url to continue to have an image as a representation of them and then a seperate profile page
    # It won't show the saved insults and stuff but more to show like a profile of the person. IDK

    image_url = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
