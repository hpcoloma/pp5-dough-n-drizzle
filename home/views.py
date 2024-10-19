from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm, NewsletterSubscriptionForm
from .models import NewsletterSubscription

# Create your views here.

def index(request):
    """A view to retunr the index page"""
    
    show_newsletter_modal = False

    # Check if the user is logged in
    if request.user.is_authenticated:
        user_email = request.user.email
        
        # Check if the user's email is already subscribed to the newsletter
        if not NewsletterSubscription.objects.filter(email=user_email).exists():
            show_newsletter_modal = True

    # Pass the flag to the context
    context = {
        'show_newsletter_modal': show_newsletter_modal
    }

    return render(request, 'home/index.html', context)


def about(request):
    return render(request, 'home/about.html')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send the email
            send_mail(
                subject=f"Contact Us Message: {subject}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=email,
                recipient_list=['doughndrizzle@gmail.com'],
                fail_silently=False,
            )

            # Display success message
            messages.success(request, 'Thank you for reaching out! We will get back to you shortly.')
            return redirect('contact_us')
    else:
        form = ContactForm()

    return render(request, 'home/contact_us.html', {'form': form})


def subscribe_newsletter(request):
    """Handles newsletter subscription."""
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save()

            # Send a confirmation email
            send_mail(
                'Welcome to Dough & Drizzle',
                'Thank you for subscribing to our newsletter! Use code WELCOME10 and enjoy 10% off on your first order.',
                'doughndrizzle@example.com', 
                [subscription.email],
                fail_silently=True,
            )
            messages.success(request, 'Thank you for subscribing!')
            return redirect('home')
        else:
            # If form is invalid, provide detailed feedback
            messages.error(request, 'Invalid email. Please try again.')
            return redirect('home')  # Or redirect to a subscription page to retry
    else:    
        return redirect('home')