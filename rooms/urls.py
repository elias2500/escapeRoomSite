from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('new/', views.CreateRoomView.as_view(), name='new'),
    path('by/<username>/', views.RoomListView.as_view(), name='for_user'),
    path('by/<username>/<pk>/', views.RoomDetailView.as_view(), name='single'),
    path('delete/<pk>/', views.DeleteRoomView.as_view(), name='delete'),
    path('update/<username>/<pk>/', views.EditRoomView.as_view(), name='update'),
    path('new/SubRoom/for/<pk>/', views.CreateSubRoomView.as_view(), name='new_sub_room'),
    path('subRoom/<pk>/by/<username>/of/room/<title>/', views.SubRoomDetailView.as_view(), name='subroom_single'),
    path('delete/subRoom/<pk>/', views.DeleteSubRoomView.as_view(), name='delete_subroom'),
    path('subRoom/update/<pk>/', views.EditSubRoomView.as_view(), name='update_subroom'),
    path('puzzle/<pk>/', views.PuzzleDetailView.as_view(), name='puzzle_single'),
    path('new/puzzle/for/<pk>/by/<username>/', views.CreatePuzzleView.as_view(), name='new_puzzle'),
    path('puzzle/<pk>/update/', views.EditPuzzleView.as_view(), name='update_puzzle'),
    path('puzzle/delete/<pk>/', views.DeletePuzzleView.as_view(), name='delete_puzzle'),
    path('solution/<pk>/',views.SolutionDetailView.as_view(), name='solution_single'),
    path('new/solution/for/<pk>/by/<username>/',views.CreateSolutionView.as_view(), name='new_solution'),
    path('solution/<pk>/update/',views.EditSolutionView.as_view(), name='update_solution'),
    path('solution/delete/<pk>/',views.DeleteSolutionView.as_view(), name='delete_solution'),
    path('reward/<pk>/',views.RewardDetailView.as_view(), name='reward_single'),
    path('new/reward/for/<pk>/by/<username>/',views.CreateRewardView.as_view(), name='new_reward'),
    path('reward/<pk>/update/',views.EditRewardView.as_view(), name='update_reward'),
    path('reward/delete/<pk>/',views.DeleteRewardView.as_view(), name='delete_reward'),
    path('hint/<pk>/',views.HintDetailView.as_view(), name='hint_single'),
    path('new/hint/for/<pk>/by/<username>/',views.CreateHintView.as_view(), name='new_hint'),
    path('hint/<pk>/update/',views.EditHintView.as_view(), name='update_hint'),
    path('hint/delete/<pk>/',views.DeleteHintView.as_view(), name='delete_hint'),
    path('api/rooms/', views.RoomListAPIView.as_view(), name='room_list'),
    path('api/subRooms/', views.SubRoomListAPIView.as_view(), name='subroom_list'),
    path('api/puzzles/', views.PuzzleListAPIView.as_view(), name='puzzle_list'),
    path('api/solutions/', views.SolutionsListAPIView.as_view(), name='solution_list'),
    path('api/rewards/', views.RewardsListAPIView.as_view(), name='reward_list'),
    path('api/hints/', views.HintsListAPIView.as_view(), name='hint_list'),
]