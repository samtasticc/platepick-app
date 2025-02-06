from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Destination

# Create your views here.

class DestinationCreate(CreateView):
    model = Destination
    fields = '__all__'
    sucess_url = '/platepick/'