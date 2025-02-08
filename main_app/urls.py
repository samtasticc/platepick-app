from django.urls import path, include
from . import views 
from .views import RestaurantListView, DestinationListView, DestinationDetailView, add_restaurant

urlpatterns = [
    # Routes will be added here
        path('platepick/create/', views.DestinationCreate.as_view(), name='platepick-create'), 
        path('platepick/restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
        path('platepick/destinations/', DestinationListView.as_view(), name='destination-list'),
        path('platepick/destinations/<int:pk>/', DestinationDetailView.as_view(), name='platepick-detail'),
        path('platepick/destinations/<int:pk>/add-restaurant/', add_restaurant, name='add-restaurant'),
]