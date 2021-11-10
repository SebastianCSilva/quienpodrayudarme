from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('home', views.home, name='home'),
    path('categorias', views.categorias_lista, name='categorias_lista'),
    path('registrar', views.registrar, name='registrar'),
    path('login', views.login_pagina, name='login'),
    path('logout', views.logout_usuario, name='logout'),
    #
    path('maestros/', views.maestros_lista, name='maestros_lista'),
    path('maestro/<int:pk>/', views.maestro_solicitudes, name='maestro_solicitudes')
    #path('maestros/<int:pk>/', views.maestro_solicitudes, name='maestro_solicitudes')


]