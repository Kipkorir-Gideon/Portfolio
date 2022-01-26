from django.shortcuts import render
from .models import *
import os

# Create your views here.
def home(request):
    projects = Projects.objects.all()
    return render(request, 'home.html', {'projects': projects})

def project(request, project_id):
    project = Projects.objects.get(id=project_id)
    languages = Languages.objects.filter(project = project)
    return render(request, 'home.html', {'project': project, 'languages': languages})