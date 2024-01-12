from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('poll_result', views.pollin_unit_result, name='poll-result')
]
