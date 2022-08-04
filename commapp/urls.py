from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main, name="main"),
    path('board/', views.board, name="board"),
    path('board/new/', views.board_post, name="board_post"),
    path('board/<int:pk>/', views.board_detail, name="board_detail"),
    path('board_update/<int:pk>/', views.board_update, name="board_update"),
    path('board_delete/<int:pk>', views.board_delete, name="board_delete"),
    path('board/<int:pk>/comment', views.board_comment, name="board_comment"),
] 