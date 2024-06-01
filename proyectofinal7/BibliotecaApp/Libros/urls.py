from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('nuevo/', views.añadir_libro, name='añadir_libro'),
    path('modificar/<int:pk>/', views.modificar_libro, name='modificar_libro'),
    path('eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),
]
