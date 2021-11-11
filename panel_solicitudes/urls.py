from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('home', views.home, name='home'),
    path('categorias', views.categorias_lista, name='categorias_lista'),
    #
    path('registrar', views.registrar, name='registrar'),
    path('login', views.login_pagina, name='login'),
    path('logout', views.logout_usuario, name='logout'),
    #
    path('maestros/', views.maestros_lista, name='maestros_lista'),
    path('maestro/<int:pk>/', views.maestro_solicitudes, name='maestro_solicitudes'),
    #path('maestros/<int:pk>/', views.maestro_solicitudes, name='maestro_solicitudes')
    #
    #path('maestro/<int:pk>/new', views.solicitud_nueva, name='solicitud_nueva'),
    #path('maestro/<int:pk>/<int:pk>/editar', views.solicitud_detalle, name='solicitud_detalle'),
    #
    path('solicitudes/',views.solicitud_lista, name='solicitud_lista.html'),
    path('solicitud/<int:pk>/', views.solicitud_detalle, name='solicitud_detalle'),
    path('solicitud/nueva', views.solicitud_nueva, name='solicitud_nueva'),
    path('solicitud/<int:pk>/editar/', views.solicitud_editar, name='solicitud_editar'),
]