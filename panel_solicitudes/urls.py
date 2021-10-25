from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('maestros', views.maestros_lista, name='maestros_lista'),
    path('categorias', views.categorias_lista, name='categorias_lista'),
   
]