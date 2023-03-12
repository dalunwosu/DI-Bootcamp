from django.shortcuts import render
from .models import Gif, Category
from .forms import CategoryForm, GifForm

def homepage(request): 
    gifs =  Gif.objects.all() 
    context = {'gifs' : gifs}

    data = request.GET
    like_id = data.get('LIKE')
    dislike_id = data.get('DISLIKE')
    if like_id:
        add_like(int(like_id))
    if dislike_id:
        dislike(int(dislike_id))
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

    data = request.GET
    like_id = data.get('LIKE')
    dislike_id = data.get('DISLIKE')
    if like_id:
        add_like(int(like_id))
    if dislike_id:
        dislike(int(dislike_id))
    return render (request, 'new_categories.html', context)

def new_gif(request):

    if request.method == 'POST':
        form = GifForm(request.POST)
        form.save()

    gifs =  Gif.objects.all() 
    form = GifForm()

    context = {'form': form, 'gifs': gifs}

    data = request.GET
    like_id = data.get('LIKE')
    dislike_id = data.get('DISLIKE')
    if like_id:
        add_like(int(like_id))
    if dislike_id:
        dislike(int(dislike_id))
    return render (request, 'new_gifs.html', context)

def add_like(gif_id: int):
    gif = Gif.objects.get(id=gif_id)
    gif.likes += 1
    gif.save() 

def dislike(gif_id: int):
    gif = Gif.objects.get(id=gif_id)
    gif.likes -= 1
    gif.save() 