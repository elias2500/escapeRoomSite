from django.db import models
from users.models import user

# Create your models here.

class Room(models.Model):
    userId = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,default="A room")
    scenario = models.TextField(default="A scenario")
    puzzlePathDesign = models.CharField(max_length=50,default="A")
    minPlayers = models.PositiveSmallIntegerField(default=2)
    maxPlayers = models.PositiveSmallIntegerField(default=5)
    hasActor = models.BooleanField(default=False)
    goal = models.CharField(max_length=50,default="A goal")
    difficulty = models.CharField(default="Easy",max_length=10)
    timeLimit = models.TimeField(default="00:30:00")
    theme = models.CharField(default="None",max_length=50)
    brief = models.TextField(default="A brief")
    debrief = models.TextField(default="A debrief")

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