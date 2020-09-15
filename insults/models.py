from django.db import models
from authentication.models import User


# Create your models here.


class Insult(models.Model):
    text = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = 'insults'

    def __str__(self):
        return self.text
