from django.shortcuts import render
from .models import Gif, Category
from .forms import CategoryForm, GifForm

def homepage(request): 
    gifs =  Gif.objects.all() 
    context = {'gifs' : gifs}

    return render(request, 'homepage.html', context)

def category(request, id) :
    
    category = Category.objects.get(id = id)
    gifs =  category.gifs.all()

    context = {'category': category, 'gifs': gifs}

    return render(request, 'category.html', context)

def categories(request):
    
    categories = Category.objects.all()
 

    context = {'categories': categories,}

    return render(request, 'categories.html', context)

def gifs(request, id):
    gif = Gif.objects.get(id = id)
    context = {'gif': gif}

    return render(request, 'gifs.html', context)

def new_category(request):
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        form.save()
    
    categories = Category.objects.all()
    form = CategoryForm()

    context = {'form': form, "categories": categories}

    return render (request, 'new_categories.html', context)

def new_gif(request):

    if request.method == 'POST':
        form = GifForm(request.POST)
        form.save()

    gifs =  Gif.objects.all() 
    form = GifForm()

    context = {'form': form, 'gifs': gifs}

    return render (request, 'new_gifs.html', context)


