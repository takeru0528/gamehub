from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.game_list, name='game_list'),
    path('upload/', views.game_upload, name='game_upload'),
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
    path('typing/', views.typing_game, name='typing_game'),  # ← 追加！
]