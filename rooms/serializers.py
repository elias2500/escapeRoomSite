from  rest_framework import serializers
from rooms.models import Room, SubRoom, Puzzle, Reward, Solution, Hint
from users.models import User

class RoomSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='userId.username')

    class Meta:
        model = Room
        fields = ('user', 'title', 'scenario', 'puzzlePathDesign', 'minPlayers', 'maxPlayers', 'hasActor', 'goal', 'difficulty', 'timeLimit', 'theme', 'brief', 'debrief')