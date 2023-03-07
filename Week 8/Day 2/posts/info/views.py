from django.shortcuts import render
from .models import Post

def posts(request):

    all_posts = Post.objects.all()
    context: dict = {'posts': all_posts}

    # context - data that goes to html
    # template - an HTML file

    return render(request, 'posts.html', context)
