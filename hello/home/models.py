from django.db import models

# Create your models here.
class contact(models.Model):
    email = models.EmailField()
    meseges = models.TextField()