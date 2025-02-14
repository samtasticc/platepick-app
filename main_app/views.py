from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

from .restaurantForm import RestaurantForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView


from .models import Destination
from .models import Restaurant
# Create your views here.
class Home(LoginView):
    template_name = 'home.html'
    
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
            restaurant.save()  
            return redirect('platepick-detail', pk=pk)  
    else:
        form = RestaurantForm()  

    return render(request, 'restaurants/add_restaurant.html', {'form': form, 'destination': destination})

class EditDestinationView(UpdateView):
    model = Destination
    fields = ['country', 'state', 'city']
    template_name = 'destinations/edit_destination.html'
    
    def get_success_url(self):
        return reverse_lazy('platepick-detail', kwargs={'pk': self.object.pk})


class EditRestaurantView(UpdateView):
    model = Restaurant
    form_class = RestaurantForm  
    template_name = 'restaurants/edit_restaurant.html'

    def get_success_url(self):
        return reverse_lazy('platepick-detail', kwargs={'pk': self.object.destination.pk})

class DeleteRestaurantView(DeleteView):
    model = Restaurant
    template_name = 'restaurants/delete_restaurant.html'

    def get_success_url(self):
        return reverse_lazy('restaurant-list') 

class DeleteDestinationView(DeleteView):
    model = Destination
    template_name = 'destinations/delete_destination.html'
    
    def get_success_url(self):
        return reverse_lazy('destination-list')

class LandingPageView(TemplateView):
    template_name = 'landing_page.html'

class AboutView(TemplateView):
    template_name = "about.html"