from django.shortcuts import render
from .models import *
import os

# Create your views here.
def home(request):
    projects = Projects.objects.all()
    return render(request, 'home.html', {'projects': projects})