"""Gif URL Configuration

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
from gifs.views import homepage,category,categories,gifs, new_category, new_gif
urlpatterns = [
    path('admin/', admin.site.urls),
    path("homepage/", homepage, name="homepage"),
    path("category/<int:id>/", category, name="show_category"),
    path("categories/", categories, name="show_categories"),
    path("gifs/<int:id>/", gifs, name="show_gifs"),
    path("new_categories/",new_category ),
    path("new_gifs/", new_gif)
]