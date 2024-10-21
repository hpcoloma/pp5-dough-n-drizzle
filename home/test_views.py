from django.test import TestCase
from django.urls import reverse
from django.core import mail
from django.contrib.auth.models import User
from home.models import NewsletterSubscription

class HomeViewsTest(TestCase):
    
    def setUp(self):
        """Set up a test user and some initial conditions."""
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com', password='testpass')