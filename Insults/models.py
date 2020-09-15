from django.db import models

# Create your models here.

class Insult(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
