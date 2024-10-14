from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

# Create your views here.

def index(request):
    """A view to retunr the index page"""
    
    return render(request, 'home/index.html')


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