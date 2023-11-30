from typing import Any
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from braces.views import SelectRelatedMixin
from rest_framework import generics
from .permissions import OnlyOwnerCanRead
from rooms import serializers
from . import models
from django.contrib.auth import get_user_model
from . import forms
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import serializers, models


User = get_user_model()

# Create your views here.

class CreateRoomView(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.Room
    #fields = ('title', 'scenario', 'puzzlePathDesign', 'minPlayers', 'maxPlayers', 'hasActor', 'goal', 'difficulty', 'timeLimit', 'theme', 'brief', 'debrief')
    template_name = 'rooms/room_form.html'
    form_class = forms.CreateRoomForm

    #Save the object to the database and assosiate it with the current user
    def form_valid(self, form):
        #Getting the object from the form
        self.object = form.save(commit=False)
        #Setting the user of the object to the current user
        self.object.userId = self.request.user
        #Saving the object to the database
        self.object.save()
        return super().form_valid(form)   
    
    def get_success_url(self):
        return reverse('rooms:single', kwargs= {'username': self.request.user, 'pk': self.object.pk})

class RoomListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    model = models.Room

    def get_queryset(self):
        try:
            self.room_user = User.objects.prefetch_related('rooms').get(
                username__iexact=self.kwargs.get('username')
                )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.room_user.rooms.all()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["room_user"] = self.room_user
        return context
    
    def test_func(self):
        return self.request.user.username == self.kwargs.get('username')
    
class RoomDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = models.Room

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.get_object()
        subrooms = room.subRooms.all()
        context["subrooms"] = subrooms
        return context

    """ def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get('username')
        ) """

    def test_func(self):
        return self.request.user.username == self.kwargs.get('username')
    
class DeleteRoomView(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Room
    select_related = ('userId',)
    #success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse('rooms:for_user', kwargs= {'username': self.request.user})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(userId_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
    
class EditRoomView(LoginRequiredMixin, generic.UpdateView):
    #fields = ('title','noOfPlayers','difficulty','hasActor','theme','scenario','riddles')
    form_class = forms.CreateRoomForm
    model = models.Room

    def get_success_url(self):
        return reverse('rooms:single', kwargs= {'username': self.request.user, 'pk': self.object.pk})
    
class CreateSubRoomView(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.SubRoom
    template_name = 'rooms/subroom_form.html'
    form_class = forms.CreateSubRoomForm

    def form_valid(self, form):
        #Getting the object from the form
        self.object = form.save(commit=False)
        #Setting the user of the object to the current room
        self.object.roomId = get_object_or_404(models.Room, id=self.kwargs['pk'])
        #Saving the object to the database
        self.object.save()
        return super().form_valid(form)   
    
    def get_success_url(self):
        return reverse('rooms:subroom_single', kwargs= {'username': self.request.user, 'title': self.object.roomId.title, 'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = get_object_or_404(models.Room, id=self.kwargs['pk'])
        return context
    
    
class SubRoomDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = models.SubRoom
    
    def test_func(self):
        return self.request.user.username == self.kwargs.get('username')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subroom = self.get_object()
        puzzles = subroom.puzzles.all()
        context["puzzles"] = puzzles
        return context
    
class DeleteSubRoomView(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.SubRoom
    select_related = ('roomId',)
    #success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse('rooms:single', kwargs={'username': self.request.user, 'pk': self.object.roomId.pk})
    
class EditSubRoomView(LoginRequiredMixin, generic.UpdateView):
    #fields = ('title','noOfPlayers','difficulty','hasActor','theme','scenario','riddles')
    form_class = forms.CreateSubRoomForm
    model = models.SubRoom

    def get_success_url(self):
        return reverse('rooms:subroom_single', kwargs= {'username': self.request.user, 'title': self.object.roomId.title, 'pk': self.object.pk})

class CreatePuzzleView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = models.Puzzle
    template_name = 'rooms/puzzle_form.html'
    form_class = forms.CreatePuzzleForm

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['subroom'] = get_object_or_404(models.SubRoom, id=self.kwargs['pk'])
        return kwargs

    def form_valid(self, form):
        #Getting the object from the form
        self.object = form.save(commit=False)
        #Setting the user of the object to the current user
        self.object.subRoomId = get_object_or_404(models.SubRoom, id=self.kwargs['pk'])
        #Saving the object to the database
        self.object.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.username == self.kwargs.get('username')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['subroom'] = get_object_or_404(models.SubRoom, id=self.kwargs['pk'])
        return context
    
    def get_success_url(self) -> str:
        return reverse('rooms:puzzle_single', kwargs= {'pk': self.object.pk})
    
class EditPuzzleView(LoginRequiredMixin, generic.UpdateView):
    form_class = forms.CreatePuzzleForm
    model = models.Puzzle

    def get_success_url(self):
        return reverse('rooms:puzzle_single', kwargs= {'pk': self.object.pk,})
    
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['subroom'] = get_object_or_404(models.SubRoom, id=self.object.subRoomId.pk)
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['subroom'] = get_object_or_404(models.SubRoom, id=self.object.subRoomId.pk)
        return context
    
class PuzzleDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Puzzle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        puzzle = self.get_object()
        solutions = puzzle.solutions.all()
        rewards = puzzle.rewards.all()
        hints = puzzle.hints.all()
        context["solutions"] = solutions
        context["rewards"] = rewards
        context["hints"] = hints
        return context

class DeletePuzzleView(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Puzzle
    select_related = ('subRoomId',)

    def get_success_url(self):
        return reverse('rooms:subroom_single', kwargs={'username': self.request.user, 'title': self.object.subRoomId.roomId.title, 'pk': self.object.subRoomId.pk,})
    
class CreateSolutionView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = models.Solution
    template_name = 'rooms/solution_form.html'
    form_class = forms.CreateSolutionForm

    def form_valid(self, form):
        #Getting the object from the form
        self.object = form.save(commit=False)
        #Setting the user of the object to the current user
        self.object.puzzleId = get_object_or_404(models.Puzzle, id=self.kwargs['pk'])
        #Saving the object to the database
        self.object.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.username == self.kwargs.get('username')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['puzzle'] = get_object_or_404(models.Puzzle, id=self.kwargs['pk'])
        return context
    
    def get_success_url(self) -> str:
        return reverse('rooms:solution_single', kwargs= {'pk': self.object.pk})
    
class SolutionDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Solution

class DeleteSolutionView(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Solution
    select_related = ('puzzleId',)

    def get_success_url(self):
        return reverse('rooms:puzzle_single', kwargs={'pk': self.object.puzzleId.pk,})
    
class EditSolutionView(LoginRequiredMixin, generic.UpdateView):
    form_class = forms.CreateSolutionForm
    model = models.Solution

    def get_success_url(self):
        return reverse('rooms:solution_single', kwargs= {'pk': self.object.pk,})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['puzzle'] = get_object_or_404(models.Puzzle, id=self.object.puzzleId.pk)
        return context
    
class RewardDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Reward

class CreateRewardView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = models.Reward
    template_name = 'rooms/reward_form.html'
    form_class = forms.CreateRewardForm

    def form_valid(self, form):
        #Getting the object from the form
        self.object = form.save(commit=False)
        #Setting the user of the object to the current user
        self.object.puzzleId = get_object_or_404(models.Puzzle, id=self.kwargs['pk'])
        #Saving the object to the database
        self.object.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.username == self.kwargs.get('username')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['puzzle'] = get_object_or_404(models.Puzzle, id=self.kwargs['pk'])
        return context
    
    def get_success_url(self) -> str:
        return reverse('rooms:reward_single', kwargs= {'pk': self.object.pk})

class EditRewardView(LoginRequiredMixin, generic.UpdateView):
    form_class = forms.CreateRewardForm
    model = models.Reward

    def get_success_url(self):
        return reverse('rooms:reward_single', kwargs= {'pk': self.object.pk,})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['puzzle'] = get_object_or_404(models.Puzzle, id=self.object.puzzleId.pk)
        return context
    
class DeleteRewardView(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Reward
    select_related = ('puzzleId',)

    def get_success_url(self):
        return reverse('rooms:puzzle_single', kwargs={'pk': self.object.puzzleId.pk,})
    
class HintDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Hint

class CreateHintView(LoginRequiredMixin, UserPassesTestMixin, generic.CreateView):
    model = models.Hint
    template_name = 'rooms/hint_form.html'
    form_class = forms.CreateHintForm

    def form_valid(self, form):
        #Getting the object from the form
        self.object = form.save(commit=False)
        #Setting the user of the object to the current user
        self.object.puzzleId = get_object_or_404(models.Puzzle, id=self.kwargs['pk'])
        #Saving the object to the database
        self.object.save()
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.username == self.kwargs.get('username')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['puzzle'] = get_object_or_404(models.Puzzle, id=self.kwargs['pk'])
        return context
    
    def get_success_url(self) -> str:
        return reverse('rooms:hint_single', kwargs= {'pk': self.object.pk})
    
class EditHintView(LoginRequiredMixin, generic.UpdateView):
    form_class = forms.CreateHintForm
    model = models.Hint

    def get_success_url(self):
        return reverse('rooms:hint_single', kwargs= {'pk': self.object.pk,})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['puzzle'] = get_object_or_404(models.Puzzle, id=self.object.puzzleId.pk)
        return context
    
class DeleteHintView(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Hint
    select_related = ('puzzleId',)

    def get_success_url(self):
        return reverse('rooms:puzzle_single', kwargs={'pk': self.object.puzzleId.pk,})
    
class RoomListAPIView(generics.ListAPIView):
    serializer_class = serializers.RoomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return models.Room.objects.filter(userId=user)

    serializer_class = serializers.RoomSerializer