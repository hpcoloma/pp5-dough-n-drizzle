from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PoAzTRpXgL0dcIZaUzZAd0t07HJCM6Z60IQb0E98JB6mm8GUqoI6L4oXKeWEzwfW4SXykTOCRqGus3Z7r0GWiEH00W95BZPwz',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)