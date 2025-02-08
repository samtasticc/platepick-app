from django.urls import path, include
from . import views 
from .views import RestaurantListView

urlpatterns = [
    # Routes will be added here
        path('platepick/create/', views.DestinationCreate.as_view(), name='platepick-create'), 
        path('platepick/restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
]