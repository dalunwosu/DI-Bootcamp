from django.contrib import admin
from .models import Listings
@admin.register(Listings)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_listed', 'price', 'list_date','realtor']
    list_display_links = ['id', 'title']
    list_filter = ['realtor']
    list_editable = ['is_listed']
    search_fields = ['title', 'description', 'address', 'city', 'state', 'zipcode', 'price']
    list_per_page = 20
# admin.site.register(Listings)
