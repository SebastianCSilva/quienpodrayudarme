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
    path('maestro_solicitudes/<int:pk>/', views.maestro_solicitudes, name='maestro_solicitudes'),
    #
    path('maestro/<int:pk>/', views.maestro_detalle, name='maestro_detalle'),
    path('maestro/nueva', views.maestro_nueva, name='maestro_nueva'),
    path('maestro/<int:pk>/editar/', views.maestro_editar, name='maestro_editar'),

    #path('maestros/<int:pk>/', views.maestro_solicitudes, name='maestro_solicitudes')
    #
    #path('maestro/<int:pk>/new', views.solicitud_nueva, name='solicitud_nueva'),
    #path('maestro/<int:pk>/<int:pk>/editar', views.solicitud_detalle, name='solicitud_detalle'),
    #
    path('solicitudes/',views.solicitud_lista, name='solicitud_lista.html'),
    path('solicitud/<int:pk>/', views.solicitud_detalle, name='solicitud_detalle'),
    path('solicitud/nueva', views.solicitud_nueva, name='solicitud_nueva'),
    path('solicitud/<int:pk>/editar/', views.solicitud_editar, name='solicitud_editar'),
    #
    path('usuarios/',views.usuario_lista, name='usuario_lista.html'),
    path('usuario/<int:pk>/', views.usuario_detalle, name='usuario_detalle'),
    path('usuario/nueva', views.usuario_nueva, name='usuario_nueva'),
    path('usuario/<int:pk>/editar/', views.usuario_editar, name='usuario_editar'),
    # Urls personales para usuarios
    path('mis-usuarios/', views.mis_usuarios, name='mis_usuarios'),
    path('mis-maestros/', views.mis_maestros, name='mis_maestros'),
    path('mis-solicitudes/', views.mis_solcitudes, name='mis_solcitudes'),
]