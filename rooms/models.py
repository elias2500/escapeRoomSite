import datetime
from typing import Any
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

# Create your models here.

User = get_user_model()

CHOICES_LIST = [
    ('linear', 'Linear'),
    ('multiLinear', 'Multi-Linear'),
    ('open', 'Open'),
]

class Room(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms')
    title = models.CharField(max_length=50, blank=True, unique=True)
    scenario = models.TextField(blank=True)
    puzzlePathDesign = models.CharField(max_length=50,blank=True, choices=CHOICES_LIST)
    minPlayers = models.PositiveSmallIntegerField(blank=True, validators = [MinValueValidator(1)])
    #TODO: Problem: maxPlayers can't be less than minPlayers but I can't directly compare a PositiveSmallIntegerField to an integer.
    maxPlayers = models.PositiveSmallIntegerField(blank=True) #, validators = [MinValueValidator(int(minPlayers))]
    hasActor = models.BooleanField(default=False)
    goal = models.CharField(max_length=50,blank=True)
    difficulty = models.CharField(blank=True,max_length=50)
    #Changed timeLimit froma a TimeField to a DurationField
    timeLimit = models.DurationField(blank=True)
    theme = models.CharField(blank=True,max_length=50)
    brief = models.TextField(blank=True)
    debrief = models.TextField(blank=True)

    class Meta:
        unique_together = ['userId','title']

class SubRoom(models.Model):
    roomId = models.ForeignKey(Room, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,default="A subroom")

class Puzzle(models.Model):
    subRoomId = models.ForeignKey(SubRoom, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,default="A puzzle")
    relatedPuzzle = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

class Solution(models.Model):
    puzzleId = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    description = models.TextField(default="A description")

class Reward(models.Model):
    puzzleId = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    description = models.TextField(default="A description")

class Hint(models.Model):
    puzzleId = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    description = models.TextField(default="A description")