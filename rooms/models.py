import datetime
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Room(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms')
    title = models.CharField(max_length=50,default="A room", unique=True)
    scenario = models.TextField(default="A scenario")
    puzzlePathDesign = models.CharField(max_length=50,default="A")
    minPlayers = models.PositiveSmallIntegerField(default=2)
    maxPlayers = models.PositiveSmallIntegerField(default=5)
    hasActor = models.BooleanField(default=False)
    goal = models.CharField(max_length=50,default="A goal")
    difficulty = models.CharField(default="Easy",max_length=10)
    #Changed timeLimit froma a TimeField to a DurationField
    timeLimit = models.DurationField(default=datetime.timedelta(minutes=60))
    theme = models.CharField(default="None",max_length=50)
    brief = models.TextField(default="A brief")
    debrief = models.TextField(default="A debrief")

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