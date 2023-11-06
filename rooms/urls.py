from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('new/', views.CreateRoomView.as_view(), name='new'),
    path('by/<username>/', views.RoomListView.as_view(), name='for_user'),
    path('by/<username>/<pk>/', views.RoomDetailView.as_view(), name='single'),
    path('delete/<pk>/', views.DeleteRoomView.as_view(), name='delete'),
    path('update/<username>/<pk>/', views.EditRoomView.as_view(), name='update'),
]
