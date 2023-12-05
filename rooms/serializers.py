from  rest_framework import serializers
from rooms.models import Room, SubRoom, Puzzle, Reward, Solution, Hint
from users.models import User
from django.contrib.auth import get_user_model

class RoomSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='userId.username')
    subRooms = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Room
        fields = ('user', 'title', 'scenario', 'puzzlePathDesign', 'minPlayers', 'maxPlayers', 'hasActor', 'goal', 'difficulty', 'timeLimit', 'theme', 'brief', 'debrief', 'subRooms')

class SubRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRoom
        fields = ('title' ,'puzzles')

class PuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puzzle
        fields = ('title', 'description', 'relatedPuzzle', 'solutions', 'rewards', 'hints')

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('puzzleId', 'description',)

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ('puzzleId', 'description',)

class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hint
        fields = ('puzzleId', 'description', 'condition')