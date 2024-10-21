from django.test import TestCase
from .forms import OrderForm
from .models import Order


class OrderFormTest(TestCase):

    def test_order_form_valid_data(self):
        """Test the order form with valid data."""
        form_data = {
            'full_name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Main St',
            'street_address2': 'Apt 4B',
            'town_or_city': 'Anytown',
            'postcode': '12345',
            'country': 'US',
            'county': 'County Name',
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['full_name'], 'John Doe')
    
    def test_order_form_field_attributes(self):
        """Test the form's field attributes."""
        form = OrderForm()
        self.assertEqual(form.fields['full_name'].widget.attrs['placeholder'], 'Full Name *')
        self.assertTrue(form.fields['full_name'].widget.attrs['autofocus'])
        self.assertEqual(form.fields['phone_number'].widget.attrs['class'], 'stripe-style-input')
    
    def test_order_form_placeholder_for_non_required_field(self):
        """Test placeholder for non-required field."""
        form = OrderForm()
        self.assertEqual(form.fields['street_address2'].widget.attrs['placeholder'], 'Street Address 2')
    
    def test_order_form_label_is_false(self):
        """Test if labels are set to false for all fields."""
        form = OrderForm()
        for field in form.fields:
            self.assertFalse(form.fields[field].label)



