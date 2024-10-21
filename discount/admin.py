from django.contrib import admin
from .models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_type', 'amount',
                    'active', 'expiration_date')
    list_filter = ('discount_type', 'active')
    search_fields = ('code',)
    ordering = ('-expiration_date',)
    actions = ['activate_discounts', 'deactivate_discounts']

    def activate_discounts(self, request, queryset):
        queryset.update(active=True)
        self.message_user(request, "Selected discounts have been activated.")
    activate_discounts.short_description = 'Activate selected discounts'

    def deactivate_discounts(self, request, queryset):
        queryset.update(active=False)
        self.message_user(request, "Selected discounts have been deactivated.")
    deactivate_discounts.short_description = 'Deactivate selected discounts'
