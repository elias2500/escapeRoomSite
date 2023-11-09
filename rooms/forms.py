from django import forms
from . import models

class CreateRoomForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'scenario', 'puzzlePathDesign', 'minPlayers', 'maxPlayers', 'hasActor', 'goal', 'difficulty', 'timeLimit', 'theme', 'brief', 'debrief')
        model = models.Room

    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args,**kwargs)

class CreateSubRoomForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'roomId')
        model = models.SubRoom

    roomId = forms.ModelChoiceField(queryset=None,
                                      empty_label=None,
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='Room')

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['roomId'].queryset = request.user.rooms.all()
        self.fields['roomId'].label_from_instance = lambda obj: obj.title