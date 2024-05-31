from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_libros, name='listar_libros'),
    path('crear/', views.crear_libro, name='crear_libro'),
]
