from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('new/', views.CreateRoomView.as_view(), name='new'),
    path('by/<username>/', views.RoomListView.as_view(), name='for_user'),
]
