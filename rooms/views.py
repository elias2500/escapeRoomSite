from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from . import models

# Create your views here.

class CreateRoomView(generic.CreateView, LoginRequiredMixin, SelectRelatedMixin):
    fields = ('name', 'description', 'difficulty', 'time_limit', 'min_players', 'max_players')
    model = models.Room
    

class RoomListView(generic.ListView):
    model = models.Room
    select_related = ('user',)
    template_name = 'rooms/room_list.html'