from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. \n'
        'A confirmation email was sent on the order date.\n'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
        'from_odrder_history': True,
    }

    return render(request, template, context)


@login_required
def admin_management(request):
    """ Display the admin management options. """
    if not request.user.is_superuser:
        return redirect('home')  # Redirect non-superusers to home

    context = {}
    return render(request, 'profiles/admin_management.html', context)


@login_required
def order_history_list(request):
    """ Display the user's order history. """
    # Fetch the user's profile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Fetch all orders associated with the user's profile
    orders = Order.objects.filter(user_profile=profile).order_by('-date')

    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def order_management(request):
    """ View for staff to manage all orders. """
    if not request.user.is_staff:
        messages.error(request,
                       "You do not have permission to access this page.")
        return redirect('home')  # Redirect if not a staff member

    # Get the status filter from the request
    status_filter = request.GET.get('status', None)

    # Fetch all orders, applying the status filter if it's set
    orders = Order.objects.all()
    if status_filter:
        orders = orders.filter(status=status_filter)

    # Pass the filter option to the template
    context = {
        'orders': orders,
        'status_filter': status_filter,
    }

    return render(request, 'profiles/order_management.html', context)


@login_required
def update_order_status(request, order_number):
    """ Update the status of a specific order. """
    if not request.user.is_staff:
        messages.error(request,
                       "You do not have permission to access this page.")
        return redirect('home')  # Redirect if not a staff member

    order = get_object_or_404(Order, order_number=order_number)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            messages.success(
                request,
                f'Status of order {order_number} updated to {new_status}.'
            )

        else:
            messages.error(request, 'Invalid status selected.')

    return redirect('order_management')


@login_required
def delete_order(request, order_number):
    """ Delete a specific order if the user is a superuser. """
    if not request.user.is_superuser:
        messages.error(request,
                       "You do not have permission to delete this order.")
        return redirect('order_management')

    order = get_object_or_404(Order, order_number=order_number)
    order.delete()
    messages.success(
        request,
        f'Order {order_number} has been deleted successfully.'
        )

    return redirect('order_management')
