"""FilmProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from films.views import add_director, addfilm, homepage, UpdateDirectorView, UpdateFilmView, DeleteDirectorView, DeleteFilmView, film
from accounts.views import IMDILoginView, IMDILogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addFilm/', addfilm, name= 'add_film'),
    path('addDirector/',add_director, name='add_director'),
    path('homepage/', homepage, name='homepage'),
    path('updatefilm/<int:pk>/', UpdateFilmView.as_view(), name='update_film'),
    path('updatedirector/<int:pk>/', UpdateDirectorView.as_view(), name='update_director'),
    path('deletefilm/<int:pk>/', DeleteFilmView.as_view(), name='delete_film'),
    path('deletedirector/<int:pk>/', DeleteDirectorView.as_view(), name='delete_director'),
    path('film/<int:id>', film, name='film' ),
    path('login/', IMDILoginView.as_view(), name='login'),
    path('logout/', IMDILogoutView.as_view(), name='logout')
]
