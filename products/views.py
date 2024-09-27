from django.shortcuts import render
from .models import Product, Category

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    categories = Category.objects.all()
    products_by_category = {}

    for category in categories:
        products_by_category[category] = Product.objects.filter(category=category)

    context = {
        'products_by_category': products_by_category,
    }

    return render(request, 'products/products.html', context)