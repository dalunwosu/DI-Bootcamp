from django.contrib import admin
from django.urls import path
from posts.views import about, posts, profile, post

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", about),
    path("posts/", posts), 
    path("profile_user/", profile),
    path("post/<int:id>", post)
]
