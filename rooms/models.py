from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user(User):
    pass

class Room(models.Model):
    User_ID = models.ForeignKey(user, on_delete=models.CASCADE)
    Title = models.CharField()
    Scenario = models.TextField()
    PuzzlePathDesign = models.CharField()
    MinPlayers = models.PositiveSmallIntegerField()
    MaxPlayers = models.PositiveSmallIntegerField()