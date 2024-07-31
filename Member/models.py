# models.py
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    photo = models.ImageField(upload_to='members/')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
