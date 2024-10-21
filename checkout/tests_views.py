from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile
from products.models import Product
from django.conf import settings
from unittest.mock import patch
import stripe
import json


class CheckoutViewTests(TestCase):

    @patch('checkout.views.stripe.PaymentIntent.create')
    def test_checkout_view_post_valid(self, mock_payment_intent_create):
        """
        Test posting valid data to the checkout view and successful order creation.
        """
        mock_payment_intent_create.return_value = {
            'client_secret': 'test_secret'
        }

        self.client.login(username='testuser', password='testpass')

        # Post valid order form data
        response = self.client.post(reverse('checkout'), {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'country': 'US',
            'postcode': '12345',
            'town_or_city': 'Test Town',
            'street_address1': '123 Test St',
            'street_address2': '',
            'county': 'Test County',
            'client_secret': 'test_secret',
        })

        # Check that the order is created
        order = Order.objects.first()
        self.assertIsNotNone(order)
        self.assertEqual(order.full_name, 'Test User')

        # Check redirection to checkout success page
        self.assertRedirects(response, reverse('checkout_success', args=[order.order_number]))

    def test_checkout_success_view(self):
        """
        Test the checkout_success view to ensure it handles a successful checkout.
        """
        self.client.login(username='testuser', password='testpass')

        # Create a test order
        order = Order.objects.create(
            full_name="Test User",
            email="test@example.com",
            phone_number="1234567890",
            country="US",
            postcode="12345",
            town_or_city="Test Town",
            street_address1="123 Test St",
            county="Test County",
            stripe_pid="test_pid",
        )

        # Test the success view
        response = self.client.get(reverse('checkout_success', args=[order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertContains(response, 'Order successfully processed!')
        self.assertIn('order', response.context)
    
    @patch('checkout.views.stripe.PaymentIntent.modify')
    def test_cache_checkout_data(self, mock_payment_intent_modify):
        """
        Test that checkout data is cached successfully via the view.
        """
        self.client.login(username='testuser', password='testpass')

        response = self.client.post(reverse('cache_checkout_data'), {
            'client_secret': 'test_secret',
            'save_info': 'on',
        })

        self.assertEqual(response.status_code, 200)
        mock_payment_intent_modify.assert_called_once()