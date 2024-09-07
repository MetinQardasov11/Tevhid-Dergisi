from django.shortcuts import render

from django.template import TemplateDoesNotExist
from django.http import HttpResponse

# Create your views here.

def index(request):
    try:
        return render(request, 'contact/index.html')
    except TemplateDoesNotExist:
        print("Template not found")
        return HttpResponse("Template not found")