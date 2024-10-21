from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Discount
from .forms import DiscountForm


# Create
def create_discount(request):
    if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Discount code created successfully.')
            return redirect('discount_list')
    else:
        form = DiscountForm()
    return render(request, 'discount/create_discount.html', {'form': form})


# Read (list)
def discount_list(request):
    discounts = Discount.objects.all()
    return render(request, 'discount/discount_list.html',
                  {'discounts': discounts})


# Update
def edit_discount(request, discount_id):
    discount = get_object_or_404(Discount, id=discount_id)
    if request.method == 'POST':
        form = DiscountForm(request.POST, instance=discount)
        if form.is_valid():
            form.save()
            messages.success(request, 'Discount code updated successfully.')
            return redirect('discount_list')
    else:
        form = DiscountForm(instance=discount)
    return render(request, 'discount/edit_discount.html', {'form': form})


# Delete
def delete_discount(request, discount_id):
    discount = get_object_or_404(Discount, id=discount_id)
    if request.method == 'POST':
        discount.delete()
        messages.success(request, 'Discount code deleted successfully.')
        return redirect('discount_list')
    return render(request, 'discount/delete_discount.html',
                  {'discount': discount})
