from django.contrib import admin
from .models import Post, Addition, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Addition)
admin.site.register(Category)
