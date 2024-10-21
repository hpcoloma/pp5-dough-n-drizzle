from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product
from discount.models import Discount


class CartViewsTests(TestCase):
    def setUp(self):
        """Create a user and product for testing"""
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.product = Product.objects.create(name='Test Product', price=10.00)

    def test_add_to_cart(self):
        """Test adding an item to the cart"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 2,
            'redirect_url': reverse('view_cart')
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('view_cart'))
        self.assertEqual(self.client.session['cart'][str(self.product.id)], 2)

    def test_adjust_cart(self):
        """Test adjusting the quantity of a cart item"""
        self.client.login(username='testuser', password='testpass')
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 2,
            'redirect_url': reverse('view_cart')
        })
        response = self.client.post(reverse('adjust_cart', args=[self.product.id]), {
            'quantity': 3
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('view_cart'))
        self.assertEqual(self.client.session['cart'][str(self.product.id)], 3)

    def test_remove_from_cart(self):
        """Test removing an item from the cart"""
        self.client.login(username='testuser', password='testpass')
        self.client.post(reverse('add_to_cart', args=[self.product.id]), {
            'quantity': 1,
            'redirect_url': reverse('view_cart')
        })
        response = self.client.post(reverse('remove_cart', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(str(self.product.id), self.client.session['cart'])

    