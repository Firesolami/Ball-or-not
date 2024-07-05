from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ball-or-not/', views.ball_or_not, name='ball_or_not'),
]
