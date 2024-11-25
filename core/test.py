from django.test import TestCase
from django.urls import reverse

class TestLoginRequired(TestCase):
    def test_dashboard_requires_login(self):
        # Make a GET request to the dashboard page
        response = self.client.get(reverse('dashboard'))

        # Check if the response redirects to the login page
        self.assertRedirects(response, '/accounts/login/?next=/dashboard/')
