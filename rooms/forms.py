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
        fields = ('title',)
        model = models.SubRoom

    """ roomId = forms.ModelChoiceField(queryset=None,
                                      empty_label=None,
                                      widget=forms.Select(attrs={'class': 'form-control'}),
                                      label='Room') """

    """ def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['roomId'].queryset = request.user.rooms.all()
        self.fields['roomId'].label_from_instance = lambda obj: obj.title """
    

class CreatePuzzleForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'description', 'relatedPuzzle')
        model = models.Puzzle

    def __init__(self, *args, **kwargs):
        self.subroom = kwargs.pop('subroom', None)
        super().__init__(*args, **kwargs)
        self.fields['relatedPuzzle'].queryset = models.Puzzle.objects.filter(subRoomId=self.subroom)
        self.fields['relatedPuzzle'].label_from_instance = lambda obj: obj.title
        self.fields['relatedPuzzle'].required = False
        self.fields['relatedPuzzle'].empty_label = "None"

    def clean_relatedPuzzle(self):
        relatedPuzzle = self.cleaned_data.get('relatedPuzzle')
        if self.instance and relatedPuzzle == self.instance:
            raise forms.ValidationError("A puzzle can't be related to itself.")
        return relatedPuzzle
    
class CreateSolutionForm(forms.ModelForm):
    class Meta:
        fields = ('description',)
        model = models.Solution

class CreateRewardForm(forms.ModelForm):
    class Meta:
        fields = ('description',)
        model = models.Reward

class CreateHintForm(forms.ModelForm):
    class Meta:
        fields = ('description','condition')
        model = models.Hint