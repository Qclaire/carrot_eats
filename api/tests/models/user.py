from django.test import TestCase
from django.core.exceptions import ValidationError
from api.models import User

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'password': 'password',
            'role': 'customer',
        }

    def test_first_name_min_length_validator(self):
        self.user_data['first_name'] = 'J'  # Invalid: below minimum length
        with self.assertRaises(ValidationError):
            user = User(**self.user_data)
            user.full_clean()

    def test_last_name_min_length_validator(self):
        self.user_data['last_name'] = 'D'  # Invalid: below minimum length
        with self.assertRaises(ValidationError):
            user = User(**self.user_data)
            user.full_clean()

    def test_email_validator(self):
        self.user_data['email'] = 'invalid-email'  # Invalid: not a valid email address
        with self.assertRaises(ValidationError):
            user = User(**self.user_data)
            user.full_clean()

    def test_password_min_length_validator(self):
        self.user_data['password'] = 'pass'  # Invalid: below minimum length
        with self.assertRaises(ValidationError):
            user = User(**self.user_data)
            user.full_clean()

    def test_create_user(self):
        user = User.objects.create(**self.user_data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'john.doe@example.com')
        self.assertEqual(user.role, 'customer')
    
    def test_user_str_method(self):
        user = User.objects.create(**self.user_data)
        self.assertEqual(str(user), 'John Doe')
