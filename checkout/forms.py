from django import forms
from .models import Order
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)
        widgets = {
            'country': CountrySelectWidget(),  # Use the country select widget
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders, classes, remove auto-generated labels,
        set autofocus on the first field, and customize error messages.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # Add autofocus on the first field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Loop through fields and apply placeholders and classes
        for field in self.fields:
            if field != "country":
                # Set placeholders with asterisks for required fields
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

            # Add common class to all fields
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'

            # Remove labels as they will be replaced by placeholders
            self.fields[field].label = False

        # Optional: Customize error messages for required fields
        self.fields['full_name'].error_messages = {'required': 'Full name is required.'}
        self.fields['street_address1'].error_messages = {'required': 'Street Address 1 is required.'}
        self.fields['postcode'].error_messages = {'required': 'Postal code is required.'}
