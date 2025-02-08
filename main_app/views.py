from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Destination
from .forms import RestaurantForm

# Create your views here.

class DestinationCreate(CreateView):
    model = Destination
    fields = '__all__'
    sucess_url = '/platepick/'

def destination_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    restaurant_form = RestaurantForm()
    return render(request, 'platepick/detail.html', {
        'destination': destination, 'restaurant_form': restaurant_form
    }) # will need to check with Lekan's view page first