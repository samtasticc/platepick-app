from django.urls import path, include
from . import views 
from .views import Home, RestaurantListView, DestinationListView, DestinationDetailView, add_restaurant, EditDestinationView, EditRestaurantView, DeleteRestaurantView, DeleteDestinationView, AboutView

urlpatterns = [
    # Routes will be added here
        path('platepick/about', AboutView.as_view(), name='about'),
        path('platepick/', Home.as_view(), name='landing_page'),
        path('platepick/create/', views.DestinationCreate.as_view(), name='platepick-create'), 
        path('platepick/restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
        path('platepick/destinations/', DestinationListView.as_view(), name='destination-list'),
        path('platepick/destinations/<int:pk>/', DestinationDetailView.as_view(), name='platepick-detail'),
        path('platepick/destinations/<int:pk>/add-restaurant/', add_restaurant, name='add-restaurant'),
        path('platepick/destinations/<int:pk>/edit/', EditDestinationView.as_view(), name='edit-destination'),
        path('platepick/restaurants/<int:pk>/edit/', EditRestaurantView.as_view(), name='edit-restaurant'),
        path('platepick/restaurants/<int:pk>/delete/', DeleteRestaurantView.as_view(), name='delete-restaurant'),
        path('platepick/destinations/<int:pk>/delete/', DeleteDestinationView.as_view(), name='delete-destination'),
        path('accounts/signup/', views.signup, name='signup'),

]