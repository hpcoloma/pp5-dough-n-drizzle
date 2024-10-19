from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from discount.models import Discount


def cart_contents(request):
    cart_items = []
    total = Decimal(0)
    product_count = 0
    cart = request.session.get('cart', {})

     # Retrieve discount code from the session
    discount_code = request.session.get('discount_code', None)
    discount_amount = Decimal(0) 

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # Check if there's a valid discount code
    if discount_code:
        try:
            discount = Discount.objects.get(code=discount_code)
            if discount.is_valid():
                # Calculate discount amount based on the discount type
                if discount.discount_type == 'fixed':
                    discount_amount = discount.amount
                elif discount.discount_type == 'percent':
                    discount_amount = total * (discount.amount / Decimal(100))
        except Discount.DoesNotExist:
            pass  # If the discount doesn't exist, simply ignore

    # Apply discount to total
    net_total = total - discount_amount
    net_total = max(net_total, Decimal(0))  # Ensure total doesn't go below 0

    # Calculate delivery cost
    if net_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = net_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery__delta = settings.FREE_DELIVERY_THRESHOLD - net_total
    else:
        delivery = 0
        free_delivery__delta = 0

    # Calculate grand total after applying delivery charges
    grand_total = delivery + net_total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery__delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'discount_code': discount_code,
        'discount_amount': discount_amount,
    }

    return context