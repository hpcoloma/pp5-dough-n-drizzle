from django.contrib import admin
from .models import NewsletterSubscription


class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_on', 'first_order_discount')
    search_fields = ('email',)


# Register the models with the admin site
admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)