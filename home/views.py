from django.shortcuts import render

# Create your views here.

def index(request):
    """A view to retunr the index page"""
    
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html') 