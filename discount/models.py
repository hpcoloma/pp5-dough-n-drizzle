from django.db import models
from django.utils import timezone


class Discount(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_type = models.CharField(max_length=10, choices=[('fixed', 'Fixed Amount'), ('percent', 'Percentage')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    expiration_date = models.DateField(null=True, blank=True)

    def is_valid(self):
        """
        Check if the discount is still active and not expired.
        """
        return self.active and (self.expiration_date is None or self.expiration_date >= timezone.now().date())

def __str__(self):
    return self.code
