from django.shortcuts import render
from .models import Galery

# Create your views here.

def index(request):
    galeries = Galery.objects.all()
    return render(request, 'galery/galery.html', {'galeries': galeries})