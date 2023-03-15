from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AddDirectorForm, AddFilmForm
from .models import Film,Director
from django.views.generic.edit import UpdateView, DeleteView

def addfilm(request):
    errors = {}
    if request.method == 'POST':
        form_filled = AddFilmForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            return redirect('homepage')
        else:
            errors = form_filled.errors

    form = AddFilmForm()
    context = {'form': form, 'errors':errors }
    return render(request, 'addFilm.html', context)

def add_director(request):
    errors = {}
    if request.method == 'POST':
        form_filled = AddDirectorForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
            return redirect('add_film')
        else:
            errors = form_filled.errors
            
        

    form = AddDirectorForm()
    context = {'form': form, 'errors':errors }
    return render(request, 'addDirector.html', context)

def homepage(request):
    film = Film.objects.all()
    context = {"films": film}
    return render(request, 'homepage.html', context)

class UpdateFilmView(UpdateView):
    model = Film
    template_name = 'update_film.html'
    fields = '__all__'
    def get_success_url(self) -> str:
        return reverse('homepage')

class UpdateDirectorView(UpdateView):
    model = Director
    template_name = 'update_director.html'
    fields = '__all__'
    def get_success_url(self) -> str:
        return reverse('homepage')

class DeleteFilmView(DeleteView):
    model = Film
    template_name = 'delete_film.html'
    fields = '__all__'
    def get_success_url(self) -> str:
        return reverse('homepage')
    
class DeleteDirectorView(DeleteView):
    model = Director
    template_name = 'delete_director.html'
    fields = '__all__'
    def get_success_url(self) -> str:
        return reverse('homepage')

def film(request, id):
    film_obj = Film.objects.get(id=id)
    context = {"film": film_obj}
    return render(request, 'film.html', context)