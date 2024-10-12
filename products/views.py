from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

# Create your views here.
def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    categories = Category.objects.all()
    products_by_category = {}
    query = None
    selected_categories = None
    sort_by = request.GET.get('sort', 'name')

    if request.GET:
        if 'category' in request.GET:
            selected_categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=selected_categories)
            categories = Category.objects.filter(name__in=selected_categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    
    # Only sort when not filtering by category
    if not selected_categories:
        if sort_by == 'price':
            products = products.order_by('price')  # Sort by price
        elif sort_by == 'name':
            products = products.order_by('name')  # Sort by name
        elif sort_by == 'category':
            products = products.order_by('category__name')  # Sort by category

    for category in categories:
        category_products = products.filter(category=category)
        if category_products.exists():
            products_by_category[category] = category_products

    context = {
        'products_by_category': products_by_category,
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'is_filtered_by_category': bool(selected_categories),
        'sort_by': sort_by,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)