from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    categories = Category.objects.all()
    products_by_category = {}
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            category_slug = request.GET['category']
            selected_category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=selected_category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    for category in categories:
        category_products = products.filter(category=category)
        if category_products.exists():
            products_by_category[category] = category_products

    context = {
        'products_by_category': products_by_category,
        'products': products,
        'search_term': query,
        'selected_category': selected_category,
        'categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)