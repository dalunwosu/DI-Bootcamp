"""bikestore URL Configuration

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
from rent.views import customers, customer, add_customer,rentals, add_rental, vehicles, vehicle, add_vehicle,rent
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rental/<int:id>/', rent, name= 'rent'),
    path('customers/', customers, name='customers'),
    path('customer/<int:id>/', customer, name='customer'),
    path('addcustomer/', add_customer),
    path('rentals/',rentals, name='rentals'),
    path('addrental/', add_rental, name='add_rental'),
    path('vehicle/<int:id>/', vehicle, name= 'vehicle' ),
    path('vehicles/', vehicles, name='vehicles' ),
    path('addvehicle/', add_vehicle),
]
