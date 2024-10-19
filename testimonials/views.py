from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm
from orders.models import Order  # Import your Order model

@login_required
def testimonial_page(request):
    # Check if the user has made any orders
    user_orders = Order.objects.filter(user=request.user)
    
    # Fetch all approved testimonials
    testimonials = Testimonial.objects.filter(approved=True).order_by('-created_at')

    if not user_orders.exists():
        messages.error(request, "You need to have at least one completed order to add a testimonial.")
        return render(request, 'testimonials/testimonial_page.html', {'testimonials': testimonials})
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Thank you! Your testimonial has been submitted and is awaiting approval.')
            return redirect('testimonial_page')
    else:
        form = TestimonialForm()

    return render(request, 'testimonials/testimonial_page.html', {'form': form, 'testimonials': testimonials})
