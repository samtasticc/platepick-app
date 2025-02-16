from django.urls import path, include
from . import views 
from .views import Home, RestaurantListView, DestinationListView, DestinationDetailView, add_restaurant, EditDestinationView, EditRestaurantView, DeleteRestaurantView, DeleteDestinationView, AboutView


    # Routes will be added here
urlpatterns = [
    path('', Home.as_view(), name='landing_page'),  # Fix landing page
    path('about/', AboutView.as_view(), name='about'),
    path('create/', views.DestinationCreate.as_view(), name='platepick-create'), 
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('destinations/', DestinationListView.as_view(), name='destination-list'),
    path('destinations/<int:pk>/', DestinationDetailView.as_view(), name='platepick-detail'),
    path('destinations/<int:pk>/add-restaurant/', add_restaurant, name='add-restaurant'),
    path('destinations/<int:pk>/edit/', EditDestinationView.as_view(), name='edit-destination'),
    path('restaurants/<int:pk>/edit/', EditRestaurantView.as_view(), name='edit-restaurant'),
    path('restaurants/<int:pk>/delete/', DeleteRestaurantView.as_view(), name='delete-restaurant'),
    path('destinations/<int:pk>/delete/', DeleteDestinationView.as_view(), name='delete-destination'),
    path('accounts/signup/', views.signup, name='signup'),
]