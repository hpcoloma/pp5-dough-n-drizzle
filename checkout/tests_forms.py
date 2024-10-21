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
    
    def test_order_form_missing_required_fields(self):
        """Test the order form with missing required fields."""
        form_data = {
            'full_name': 'John Doe',
            'email': 'john.doe@example.com',
            'phone_number': '1234567890',
            'street_address1': '',
            'street_address2': 'Apt 4B',
            'town_or_city': 'Anytown',
            'postcode': '',
            'country': 'US',
            'county': 'County Name',
        }
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors)
        self.assertIn('street_address1', form.errors)
        self.assertIn('postcode', form.errors)
