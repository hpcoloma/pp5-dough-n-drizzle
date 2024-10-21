from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile
from checkout.models import Order

class UserProfileTests(TestCase):

    def setUp(self):
        """Set up test users, profiles, and orders."""
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com', password='testpass')
        self.superuser = User.objects.create_superuser(
            username='adminuser', email='admin@example.com', password='adminpass')
        self.staffuser = User.objects.create_user(
            username='staffuser', email='staff@example.com', password='staffpass', is_staff=True)

        # Create a user profile for the test user
        self.profile = UserProfile.objects.create(user=self.user)

        # Create a sample order for the test user
        self.order = Order.objects.create(
            order_number="123456",
            user_profile=self.profile,
            full_name="John Doe",
            total_price=100
        )