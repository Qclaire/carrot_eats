from django.test import TestCase
from django.core.exceptions import ValidationError
from api.models import Restaurant, User

class RestaurantModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            password='password',
            role='owner'
        )
        self.restaurant_data = {
            'name': 'ABC Restaurant',
            'description': 'A great place to dine.',
            'owner': self.user,
        }

    def test_name_min_length_validator(self):
        self.restaurant_data['name'] = 'A'  # Invalid: below minimum length
        with self.assertRaises(ValidationError):
            restaurant = Restaurant(**self.restaurant_data)
            restaurant.full_clean()

    def test_create_restaurant(self):
        restaurant = Restaurant.objects.create(**self.restaurant_data)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(restaurant.name, 'ABC Restaurant')
        self.assertEqual(restaurant.description, 'A great place to dine.')
        self.assertEqual(restaurant.owner, self.user)
    
    def test_restaurant_str_method(self):
        restaurant = Restaurant.objects.create(**self.restaurant_data)
        self.assertEqual(str(restaurant), 'ABC Restaurant')
