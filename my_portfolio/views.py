from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    projects = Projects.objects.all()
    return render(request, 'home.html', {'projects': projects})