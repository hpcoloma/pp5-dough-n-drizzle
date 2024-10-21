"""Error Handling"""
from django.core.exceptions import PermissionDenied
from django.shortcuts import render


def custom_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)


def custom_400_view(request, exception):
    """
    Page not found
    """
    return render(request, 'errors/400.html', status=400)


def custom_401_view(request, exception):
    """
    Not Authorised to Access
    """
    return render(request, 'errors/401.html', status=401)


def custom_403_view(request, exception):
    '''
    No permission to access this page
    '''
    if isinstance(exception, PermissionDenied):
        return render(request, 'errors/403.html', status=403)
    else:
        return render(request, 'errors/500.html', status=500)


def custom_500_view(request):
    """Custom 500 error view."""
    return render(request, 'errors/500.html', status=500)
