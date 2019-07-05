from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    api_url = models.URLField("URL de l'API Redmine", blank=True)
    api_key = models.CharField('Clé API Redmine', max_length=40, blank=True)
