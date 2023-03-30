from django.shortcuts import render
from realtors.models import Realtor
from listings.models import Listings
from listings.choices import states_choices, bedrooms_choices, prices_choices

def about(request):
    realtors = Realtor.objects.all()
    mvp_realtors = Realtor.objects.all().filter(is_MVP=True)
    context = {'realtors':realtors, 'mvp_realtors':mvp_realtors}
    return render(request,'about.html', context)

def home(request):
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
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

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

  return render(request, 'home.html', context)





