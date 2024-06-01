from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_autores, name='lista_autores'),
    path('nuevo/', views.añadir_autor, name='añadir_autor'),
    path('modificar/<int:pk>/', views.modificar_autor, name='modificar_autor'),
    path('eliminar/<int:pk>/', views.eliminar_autor, name='eliminar_autor'),
]
