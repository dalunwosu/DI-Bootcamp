from django.shortcuts import render
from .models import Customer,Vehicle,Rental,RentalRate
from .forms import CustomerForm, RentalForm, VehicleForm
from django.views.generic import ListView

def customers(request):
    customers_list = Customer.objects.all().order_by('first_name','last_name')
    context = {'customers':customers_list}
    return render (request,'customers.html',context)

def customer(request, id):
    customer_obj = Customer.objects.get(id=id)
    context = {'customer': customer_obj}
    return render(request, 'customer.html', context)

def add_customer(request):
    if request.method == 'POST':
        form_filled = CustomerForm(request.POST)
        form_filled.save()

    form = CustomerForm()
    context = {'form': form }
    return render(request, 'add_customer.html', context)

def rentals(request):
    rental_list = Rental.objects.all().order_by('-return_date', 'return_date')
    context = {'rentals':rental_list}
    return render (request,'rentals.html',context)

def add_rental(request):
    if request.method == 'POST':
        form_filled = RentalForm(request.POST)
        form_filled.save()

    form = RentalForm()
    context = {'form': form }
    return render(request, 'add_rental.html', context)

def vehicles(request):
    vehicles_list = Vehicle.objects.all().order_by('type')
    context = {'vehicles':vehicles_list}
    return render (request,'vehicles.html',context)

def vehicle(request, id):
    vehicle_obj = Vehicle.objects.get(id=id)
    context = {'vehicle': vehicle_obj}
    return render(request, 'vehicle.html', context)

def add_vehicle(request):
    if request.method == 'POST':
        form_filled = VehicleForm(request.POST)
        form_filled.save()

    form = VehicleForm()
    context = {'form': form }
    return render(request, 'add_vehicle.html', context)

def rent(request, id):
    customer_obj = Customer.objects.get(id=id)
    rental_obj = Rental.objects.get(customer_id=id)
    vehicle_obj = Vehicle.objects.get(id=rental_obj.vehicle_id)
    context = {'customer': customer_obj, 'rental':rental_obj, 'vehicle': vehicle_obj}
    return render(request, 'rental.html', context)