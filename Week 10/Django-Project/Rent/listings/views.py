from django.shortcuts import render
from .models import Listings
from django.core.paginator import Paginator
from .choices import states_choices, bedrooms_choices, prices_choices

def listings(request):
    list = Listings.objects.all().order_by('-list_date').filter(is_listed=True)
    paginator = Paginator(list,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'listings':paged_listings}
    return render(request, 'listings.html', context)

def listing(request,id):
    list = Listings.objects.get(id=id)
    context = {'listing':list}
    return render(request, 'listing.html', context)

def search(request):
  queryset_list = Listings.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedroom' in request.GET:
    bedroom = request.GET['bedroom']
    if bedroom:
      queryset_list = queryset_list.filter(bedroom__lte=bedroom)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'state_choices': states_choices,
    'bedroom_choices': bedrooms_choices,
    'price_choices': prices_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'search.html', context)

