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
    path('comment_create/<int:pk>/', views.comment_create, name="comment_create"),
    path('comment_update/<int:pk>/', views.comment_update, name="comment_update"),
    path('comment_delete/<int:pk>', views.comment_delete, name="comment_delete"),
    path('recomment_create/<int:pk>/<int:c_pk>/', views.recomment_create, name="recomment_create"),
    path('recomment_delete/<int:pk>/<int:rc_pk>/', views.recomment_delete, name="recomment_delete")
] 