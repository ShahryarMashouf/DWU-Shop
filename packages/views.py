from django.shortcuts import render
from django.http import HttpResponse
from . models import Packages, Offer


def index(request):
    packages = Packages.objects.all()
    return render(request, 'index.html', {'packages': packages})

def new_page(request):
    return HttpResponse("NEW PAGE BITCH")