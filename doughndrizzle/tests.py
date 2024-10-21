from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest


class ErrorHandlingTests(TestCase):
    
    def test_custom_404_view(self):
        """Test custom 404 view"""
        response = self.client.get('/non-existent-url/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'errors/404.html')

    def test_custom_400_view(self):
        """Test custom 400 view"""
        # Simulate a 400 error using a bad request
        request = HttpRequest()
        request.META['HTTP_USER_AGENT'] = 'invalid_user_agent'  # Simulating invalid input
        response = self.client.get(reverse('your_view_name'), data={'invalid_param': 'invalid_value'})
        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed(response, 'errors/400.html')

    def test_custom_401_view(self):
        """Test custom 401 view"""
        # Simulating unauthorized access
        request = HttpRequest()
        response = self.client.get(reverse('your_protected_view_name'))
        self.assertEqual(response.status_code, 401)
        self.assertTemplateUsed(response, 'errors/401.html')

    def test_custom_403_view(self):
        """Test custom 403 view"""
        # Simulating a PermissionDenied exception
        request = HttpRequest()
        with self.assertRaises(PermissionDenied):
            raise PermissionDenied
        response = self.client.get(reverse('your_restricted_view_name'))
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, 'errors/403.html')

