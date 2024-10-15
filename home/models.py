from django.db import models

class NewsletterSubscription(models.Model):
    """Model to store newsletter subscription."""
    email = models.EmailField(unique=True)
    subscribed_on = models.DateTimeField(auto_now_add=True)
    first_order_discount = models.BooleanField(default=True)  # For offering 10% off on first order

    def __str__(self):
        return self.email