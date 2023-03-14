from django.shortcuts import render
from .models import Map

# Create your views here.

def map(request):
    location = Map.objects.all()
    return render(request, 'map/map.html', {'location': location})