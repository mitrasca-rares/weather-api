import json
from django.shortcuts import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from ..models import Location

class TestWeatherApi(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        self.location = Location(description="my new location", user=self.user)
        self.location.save()

    def test_location_creation(self):
        url = reverse('locations')
        response = self.client.post(url, {
            'description': 'my new location'
        }, format='json')
        # assert new location was added
        self.assertEqual(Location.objects.count(), 2)

        # assert a created status code was returned
        self.assertEqual(201, response.status_code)
    
    def test_getting_locations(self):
        url = reverse('locations')
        response = self.client.get(url, format="json")
        self.assertEqual(len(json.loads(response.content)), 1)