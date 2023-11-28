import datetime
from typing import Any
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

# Create your models here.

#TODO: Consider adding age restriction.

User = get_user_model()

PUZZLE_CHOICES_LIST = [
    ('linear', 'Linear'),
    ('multiLinear', 'Multi-Linear'),
    ('open', 'Open'),
]

DIFFICULTY_CHOICES_LIST = [
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
]

class Room(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms')
    title = models.CharField(max_length=50, blank=True, unique=True)
    scenario = models.TextField(blank=True, null=True)
    puzzlePathDesign = models.CharField(max_length=50,blank=True, choices=PUZZLE_CHOICES_LIST, null=True)
    minPlayers = models.PositiveSmallIntegerField(blank=True, validators = [MinValueValidator(1)], null=True)
    #TODO: Problem: maxPlayers can't be less than minPlayers but I can't directly compare a PositiveSmallIntegerField to an integer.
    maxPlayers = models.PositiveSmallIntegerField(blank=True, null=True) #, validators = [MinValueValidator(int(minPlayers))]
    hasActor = models.BooleanField(default=False, null=True)
    goal = models.CharField(max_length=50,blank=True, null=True)
    difficulty = models.CharField(blank=True,max_length=50, choices=DIFFICULTY_CHOICES_LIST, null=True)
    #Changed timeLimit froma a TimeField to a DurationField
    timeLimit = models.DurationField(blank=True, null=True)
    theme = models.CharField(blank=True,max_length=50, null=True)
    brief = models.TextField(blank=True, null=True)
    debrief = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['userId','title']

class SubRoom(models.Model):
    roomId = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='subRooms')
    title = models.CharField(max_length=50, blank=True)

class Puzzle(models.Model):
    subRoomId = models.ForeignKey(SubRoom, on_delete=models.CASCADE, related_name='puzzles')
    title = models.CharField(max_length=50,default="A puzzle")
    description = models.TextField(default="A description", null=True)
    relatedPuzzle = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='relatedPuzzles')

class Solution(models.Model):
    puzzleId = models.ForeignKey(Puzzle, on_delete=models.CASCADE, related_name='solutions')
    description = models.TextField(default="A description")

class Reward(models.Model):
    puzzleId = models.ForeignKey(Puzzle, on_delete=models.CASCADE, related_name='rewards')
    description = models.TextField(default="A description")

class Hint(models.Model):
    puzzleId = models.ForeignKey(Puzzle, on_delete=models.CASCADE, related_name='hints')
    description = models.TextField(default="A description")
    condition = models.TextField(default="A condition")