from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Addition

def posts(request):

    all_posts = Post.objects.all()
    context: dict = {'posts': all_posts}

    # context - data that goes to html
    # template - an HTML file

    return render(request, 'posts.html', context)


def about(request):
    out = "<h1> This is a website about my posts </h1>"
    return HttpResponse(out)


def post(request, id:int):
    post = Post.objects.get(id=id)
    addon = post.addition

    context = {'post': post, 'addon': addon}

    return render(request, 'post.html', context)




def profile(request):

    context = {
        'name': 'Yossi Eik', 
        'age': 31,
        'gender': 'M',
        'hobbies': ['Python', 'Django', 'Purim']
    }

    return render(request, 'profile_user.html', context)



