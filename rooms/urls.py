from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('new/', views.CreateRoomView.as_view(), name='new'),
    path('by/<username>/', views.RoomListView.as_view(), name='for_user'),
    path('by/<username>/<pk>/', views.RoomDetailView.as_view(), name='single'),
    path('delete/<pk>/', views.DeleteRoomView.as_view(), name='delete'),
    path('update/<username>/<pk>/', views.EditRoomView.as_view(), name='update'),
    path('newSubRoom/for/<pk>', views.CreateSubRoomView.as_view(), name='new_sub_room'),
    path('subRoom/<pk>/by/<username>/of/room/<title>/', views.SubRoomDetailView.as_view(), name='subroom_single'),
    path('subRoomDelete/<pk>/', views.DeleteSubRoomView.as_view(), name='delete_subroom'),
    path('subRoom/update/<pk>/', views.EditSubRoomView.as_view(), name='update_subroom'),
]
