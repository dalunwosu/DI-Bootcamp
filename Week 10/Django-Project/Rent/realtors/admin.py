from django.contrib import admin
from .models import Realtor
@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'hire_date','is_MVP']
    list_display_links = ['id', 'name']
    list_editable = ['is_MVP']
    search_fields = ['name']
    list_per_page = 20
# admin.site.register(Realtor)
