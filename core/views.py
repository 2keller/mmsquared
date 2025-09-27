from django.shortcuts import render
from .models import PhotoPortfolio, PrintProject, TutoringPackage

def photography(request):
    photos = PhotoPortfolio.objects.all()
    return render(request, 'core/photography.html', {'photos': photos})

def printing(request):
    prints = PrintProject.objects.all()
    return render(request, 'core/printing.html', {'prints': prints})

def tutoring(request):
    packages = TutoringPackage.objects.all()
    return render(request, 'core/tutoring.html', {'packages': packages})