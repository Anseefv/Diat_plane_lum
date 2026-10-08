from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    phone=models.BigIntegerField(unique=True)



