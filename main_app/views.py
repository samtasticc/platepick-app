from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from .models import Destination
from .models import Restaurant
from .restaurantForm import RestaurantForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

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

class DestinationListView(ListView):
    model = Destination
    template_name = 'destinations/destination_restaurantlists.html'
    context_object_name = 'destinations'

class DestinationDetailView(DetailView):
    model = Destination
    template_name = 'destinations/destination_details.html'
    context_object_name = 'destination'



def add_restaurant(request, pk):
    destination = get_object_or_404(Destination, pk=pk)  

    if request.method == 'POST':
        form = RestaurantForm(request.POST)  
        if form.is_valid():
            restaurant = form.save(commit=False)  
            restaurant.destination = destination  
            restaurant.save()  # ✅ Save to database
            return redirect('platepick-detail', pk=pk)  
    else:
        form = RestaurantForm()  

    return render(request, 'restaurants/add_restaurant.html', {'form': form, 'destination': destination})