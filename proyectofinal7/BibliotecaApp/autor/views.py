from django.shortcuts import render, redirect
from .models import Autor
from .forms import AutorForm

# Create your views here.

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = AutorForm()
    return render(request, 'libros/crear_autor.html', {'form': form})
