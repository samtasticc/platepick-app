from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

from .restaurant_form import RestaurantForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Destination
from .models import Restaurant
# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('destination-list') 
        else:
            error_message = 'Invalid sign up - please try again!'
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})

   
class Home(LoginView):
    template_name = 'landing_page.html'

    def get_success_url(self):
        return reverse_lazy('destination-list')
    
class DestinationCreate(CreateView):
    model = Destination
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = '/platepick/'

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurants/restaurantIndex.html'  
    context_object_name = 'restaurants'  
    ordering = ['name']  

class DestinationListView(LoginRequiredMixin, ListView):
    model = Destination
    template_name = 'destinations/destination_restaurantlists.html'
    context_object_name = 'destinations'

    def get_queryset(self):
        return Destination.objects.filter(user=self.request.user)

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

class EditDestinationView(LoginRequiredMixin, UpdateView):
    model = Destination
    fields = ['country', 'state', 'city']
    template_name = 'destinations/edit_destination.html'

    def get_queryset(self):
        return Destination.objects.filter(user=self.request.user)
    
    def get_success_url(self):
        return reverse_lazy('platepick-detail', kwargs={'pk': self.object.pk})


class EditRestaurantView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    form_class = RestaurantForm  
    template_name = 'restaurants/edit_restaurant.html'

    def get_queryset(self):
        return Restaurant.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('platepick-detail', kwargs={'pk': self.object.destination.pk})

class DeleteRestaurantView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    template_name = 'restaurants/delete_restaurant.html'

    def get_success_url(self):
        return reverse_lazy('platepick-detail', kwargs={'pk': self.object.destination.pk}) 

class DeleteDestinationView(LoginRequiredMixin, DeleteView):
    model = Destination
    template_name = 'destinations/delete_destination.html'
    
    def get_success_url(self):
        return reverse_lazy('destination-list')


class AboutView(TemplateView):
    template_name = "about.html"