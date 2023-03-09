from django.shortcuts import render
from .models import Gif, Category

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


