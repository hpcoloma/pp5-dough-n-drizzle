"""Error Handling"""
from django.core.exceptions import PermissionDenied
from django.shortcuts import render


def custom_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)


def custom_400_view(request, exception):
    return render(request, 'errors/400.html', status=404)
