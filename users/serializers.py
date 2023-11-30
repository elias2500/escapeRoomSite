from rest_framework import serializers
from users.models import user
from rooms.models import Room

class UserSerializer(serializers.ModelSerializer):
    rooms = serializers.PrimaryKeyRelatedField(many=True, queryset=Room.objects.all())

    class Meta:
        model = user
        fields = ('id', 'username',)