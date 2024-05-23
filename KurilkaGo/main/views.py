from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def index(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def cigarettes(request, page):
    #cigarettes = Cigarette.objects.all()
    cigarettes_page = Cigarette.objects.all()[(page - 1) * 12: page * 12]
    return render(request, 'products-page.html', {"products": cigarettes_page})

def cigarette(request, id):
    this_cigarette = get_object_or_404(Cigarette, id=id)
    return render(request, 'item-page.html', {"product": this_cigarette})