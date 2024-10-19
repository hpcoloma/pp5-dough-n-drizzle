from django.shortcuts import render, reverse, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F
from decimal import Decimal

from products.models import Product
from discount.models import Discount, DiscountUsage


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
                messages.error(request, 'Discount code is not valid or has expired.')
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

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart.')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

@login_required
def apply_discount(request):
    """Apply a discount code to the cart"""
    if request.method == 'POST':
        discount_code = request.POST.get('discount_code', None)
        
        if discount_code:
            try:
                discount = Discount.objects.get(code=discount_code)

                if discount.is_valid():
                    if DiscountUsage.objects.filter(discount=discount, user=request.user).exists():
                        messages.error(request, "You have already used this discount code.", extra_tags='discount')
                        request.session.pop('discount_code', None)
                    else:
                        # Record the usage of the discount code
                        DiscountUsage.objects.create(discount=discount, user=request.user)

                        # Store the discount code in the session
                        request.session['discount_code'] = discount_code
                        messages.success(request, f'Discount code "{discount_code}" applied!', extra_tags='discount')
                else:
                    messages.error(request, 'Discount code is not valid or has expired.', extra_tags='discount')
                    request.session.pop('discount_code', None)
            except Discount.DoesNotExist:
                messages.error(request, 'Invalid discount code.', extra_tags='discount')
                request.session.pop('discount_code', None)
        else:
            messages.error(request, 'Please enter a discount code.', extra_tags='discount')

    return redirect(reverse('view_cart'))