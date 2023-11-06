from django import forms
from . import models

class CreateRoomForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'scenario', 'puzzlePathDesign', 'minPlayers', 'maxPlayers', 'hasActor', 'goal', 'difficulty', 'timeLimit', 'theme', 'brief', 'debrief')
        model = models.Room

    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args,**kwargs)