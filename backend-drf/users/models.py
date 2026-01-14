from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=["username"]
    
    def __str__(self):
        return self.email
