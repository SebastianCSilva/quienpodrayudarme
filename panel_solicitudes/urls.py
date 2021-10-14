from django.urls import path
from . import views

urlpatterns = [
    path('', views.maestros_lista, name='maestros_lista'),
]