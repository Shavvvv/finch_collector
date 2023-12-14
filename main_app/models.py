from django.db import models
from django.urls import reverse

# Create your models here.

class Finch(models.Model):
    # models.CharField are called field types if you want to google others
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name