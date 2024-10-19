from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Discount(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_type = models.CharField(max_length=10, choices=[('fixed', 'Fixed Amount'), ('percent', 'Percentage')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    expiration_date = models.DateField(null=True, blank=True)
    max_uses = models.PositiveIntegerField(default=1)
    current_uses = models.PositiveIntegerField(default=0)

    def is_valid(self):
        """
        Check if the discount is still active and not expired.
        """
        return self.active and (self.expiration_date is None or self.expiration_date >= timezone.now().date())

    def __str__(self):
        return self.code


class DiscountUsage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    used_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('discount', 'user')  # Ensure a user can only use a discount once

    def __str__(self):
        return f"{self.user.username} used {self.discount.code} on {self.used_at}"
