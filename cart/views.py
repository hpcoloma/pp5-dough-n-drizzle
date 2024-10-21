from django.shortcuts import (
    render,
    reverse,
    redirect,
    HttpResponse,
    get_object_or_404
)
from django.contrib import messages
from django.db.models import F
from decimal import Decimal

from products.models import Product
from discount.models import Discount
from checkout.models import Order


def view_cart(request):
    """A view that renders the bag contents page"""
    cart = request.session.get('cart', {})
    cart_items = []
    total = Decimal(0)
    discount_code = request.session.get('discount_code', None)
    discount_amount = 0
    net_total = Decimal(0)

    # Calculate total from cart
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
            'item_id': item_id,
        })

    # Apply discount if applicable
    if discount_code:
        try:
            discount = Discount.objects.get(code=discount_code)
            if discount.is_valid():
                if discount.discount_type == 'fixed':
                    discount_amount = discount.amount
                elif discount.discount_type == 'percent':
                    discount_amount = total * (discount.amount / 100)

                net_total = total - discount_amount

            else:
                messages.error(request, 'Discount code is not '
                                        'valid or has expired.')
                del request.session['discount_code']
        except Discount.DoesNotExist:
            messages.error(request, 'Invalid discount code.')
            del request.session['discount_code']
    else:
        # If there's no discount code, set net_total to total
        net_total = total

    # Pass total, discount details to template
    context = {
        'cart_items': cart_items,
        'total': total,
        'net_total': net_total,
        'discount_code': discount_code,
        'discount_amount': discount_amount,
    }
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    # Retrieve the product or return a 404 error if not found
    product = get_object_or_404(Product, pk=item_id)

    # Get the quantity from the request, default to 1 if not provided
    quantity = request.POST.get('quantity', '1')

    # Validate the quantity
    try:
        quantity = int(quantity)
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
    except ValueError as e:
        messages.error(request, str(e), extra_tags='cart_action')
        return redirect(request.POST.get('redirect_url', 'products'))

    # Retrieve the cart from the session
    cart = request.session.get('cart', {})

    # Update the cart with the specified quantity
    if item_id in cart:
        cart[item_id] += quantity
        messages.success(
            request,
            f'Updated quantity of {product.name} to {cart[item_id]}.',
            extra_tags='cart_action'
        )
    else:
        cart[item_id] = quantity
        messages.success(
            request, f'Added {product.name} to your cart.',
            extra_tags='cart_action'
        )

    # Save the updated cart back to the session
    request.session['cart'] = cart

    # Redirect back to the specified URL or a default URL
    return redirect(request.POST.get('redirect_url', 'products'))


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}',
            extra_tags='cart_action'
            )
    else:
        cart.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from your cart',
            extra_tags='cart_action'
            )

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(
            request, f'Removed {product.name} from your cart',
            extra_tags='cart_action'
            )

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
