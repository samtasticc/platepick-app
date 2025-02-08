from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Destination
from .models import Restaurant

# Create your views here.

class DestinationCreate(CreateView):
    model = Destination
    fields = '__all__'
    sucess_url = '/platepick/'

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurants/restaurantIndex.html'  
    context_object_name = 'restaurants'  
    ordering = ['name']  