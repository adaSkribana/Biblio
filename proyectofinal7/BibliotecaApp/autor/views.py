from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Autor
from .forms import AutorForm

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'autor/lista_autores.html', {'autores': autores})

def añadir_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'autor/autor_form.html', {'form': form})

def modificar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'autor/autor_form.html', {'form': form})

def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'autor/autor_confirm_delete.html', {'autor': autor})
