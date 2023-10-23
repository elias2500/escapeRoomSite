from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from . import models

# Create your views here.

class CreateRoomView(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.Room
    fields = ('title', 'scenario', 'puzzlePathDesign', 'minPlayers', 'maxPlayers', 'hasActor', 'goal', 'difficulty', 'timeLimit', 'theme', 'brief', 'debrief')
    template_name = 'rooms/room_form.html'
    success_url = '/' #TODO: Properly redirect to the singel room page later
    
    #Save the object to the database and assosiate it with the current user
    def form_valid(self, form):
        #Getting the object from the form
        self.object = form.save(commit=False)
        #Setting the user of the object to the current user
        self.object.userId = self.request.user
        #Saving the object to the database
        self.object.save()
        return super().form_valid(form)    

class RoomListView(generic.ListView):
    model = models.Room
    select_related = ('user',)
    template_name = 'rooms/room_list.html'