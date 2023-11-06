from typing import Any
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from braces.views import SelectRelatedMixin
from . import models
from django.contrib.auth import get_user_model
from . import forms

User = get_user_model()

# Create your views here.

class CreateRoomView(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.Room
    #fields = ('title', 'scenario', 'puzzlePathDesign', 'minPlayers', 'maxPlayers', 'hasActor', 'goal', 'difficulty', 'timeLimit', 'theme', 'brief', 'debrief')
    template_name = 'rooms/room_form.html'
    success_url = '/' #TODO: Properly redirect to the singel room page later
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
    
class EditRoomView(LoginRequiredMixin, SelectRelatedMixin, generic.UpdateView):
    fields = ('title','noOfPlayers','difficulty','hasActor','theme','scenario','riddles')
    model = models.Room