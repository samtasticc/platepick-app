from django.urls import path, include
from . import views 

urlpatterns = [
    # Routes will be added here
        path('platepick/create/', views.DestinationCreate.as_view(), name='platepick-create'), 
]