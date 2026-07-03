"""URL routing configuration for the GameHub demo app."""

from django.urls import path
from . import views

app_name = 'game_hub'

urlpatterns = [
    path('', views.game_hub_view, name='home'),
]
