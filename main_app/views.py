from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView #Is this too high?
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Destination
from .models import Restaurant
from .restaurantForm import RestaurantForm
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView

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
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


class DestinationCreate(LoginRequiredMixin, CreateView):
    model = Destination
    fields = ['country', 'state', 'city']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    sucess_url = '/platepick/'

class RestaurantListView(LoginRequiredMixin, ListView):
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

class DestinationDetailView(LoginRequiredMixin, DetailView):
    model = Destination
    template_name = 'destinations/destination_details.html'
    context_object_name = 'destination'


@login_required
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
    
    def get_success_url(self):
        return reverse_lazy('platepick-detail', kwargs={'pk': self.object.pk})

class EditRestaurantView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    form_class = RestaurantForm  
    template_name = 'restaurants/edit_restaurant.html'

    def get_success_url(self):
        return reverse_lazy('platepick-detail', kwargs={'pk': self.object.destination.pk})

class DeleteDestinationView(LoginRequiredMixin, DeleteView):
    model = Destination
    template_name = 'destinations/destination_confirm_delete.html'
    success_url = reverse_lazy('destination-list')

class DeleteRestaurantView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    template_name = 'restaurants/restaurant_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('platepick-detail', kwargs={'pk': self.object.destination.pk})

class LandingPageView(LoginView):
    template_name = 'landing_page.html'

class AboutView(TemplateView):
    template_name = "about.html"