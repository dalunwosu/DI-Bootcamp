from django.shortcuts import render
from django.http import HttpResponse

def some_text(request):
    """"Shows a text on screen inside browser"""
    return HttpResponse('SOME TEXT')

def about(request):
    """"Gives a description about the page"""
    return HttpResponse('<h1>This is a page about Chukwudalu Nwosu')

def posts(request):
    author = 'Dalu'
    title = 'My first post'
    body = 'Some text about my post etc.'

    context: dict = {'author': author, 'title': title, 'body': body}

    return render(request, 'posts.html',context)

def profile(request):
    
    context = {
        'name': "Dalu Nwosu",
        'age': 17,
        'gender': "M",
        'hobbies': ['Gaming','Reading','Sports']
    }

    return render(request,'profile_user.html',context)