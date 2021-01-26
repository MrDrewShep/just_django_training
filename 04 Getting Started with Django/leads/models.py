from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey(
        "Agent", 
        on_delete=models.SET_DEFAULT, 
        default="n/a"
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


""" Example of choices in a field
class Example(models.Model):

    SOURCE_CHOICES = (
        # (valueStoredInDb, displayValue)
        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
    )

    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
"""    