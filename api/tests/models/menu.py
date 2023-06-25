from django.test import TestCase
from django.core.exceptions import ValidationError
from api.models import Restaurant, Menu, User

class MenuModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'password',
            'role': 'customer',
        }
        self.user = User.objects.create(**self.user_data)
        self.restaurant = Restaurant.objects.create(
            name='ABC Restaurant',
            description='A great place to dine.',
            owner_id=self.user.id
        )
        self.menu_data = {
            'name': 'Burger',
            'description': 'Delicious burger',
            'price': 10,
            'restaurant': self.restaurant,
        }

    def test_name_min_length_validator(self):
        self.menu_data['name'] = 'B'  # Invalid: below minimum length
        with self.assertRaises(ValidationError):
            menu = Menu(**self.menu_data)
            menu.full_clean()

    def test_price_min_value_validator(self):
        self.menu_data['price'] = -5  # Invalid: below minimum value
        with self.assertRaises(ValidationError):
            menu = Menu(**self.menu_data)
            menu.full_clean()

    def test_create_menu(self):
        menu = Menu.objects.create(**self.menu_data)
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(menu.name, 'Burger')
        self.assertEqual(menu.description, 'Delicious burger')
        self.assertEqual(menu.price, 10)
        self.assertEqual(menu.restaurant, self.restaurant)
    
    def test_menu_str_method(self):
        menu = Menu.objects.create(**self.menu_data)
        self.assertEqual(str(menu), 'Burger')
