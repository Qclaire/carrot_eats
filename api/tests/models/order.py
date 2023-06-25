from django.test import TestCase
from api.models import User, Restaurant, Order, Menu

class OrderModelTestCase(TestCase):
    def setUp(self):
        self.customer = User.objects.create(
            first_name='Test',
            last_name='User',
            email='test@example.com',
            password='testpassword'
        )
        self.restaurant = Restaurant.objects.create(
            name='ABC Restaurant',
            description='A great place to dine.',
            owner_id=1
        )
        self.menu = Menu.objects.create(
            name='Burger',
            description='Delicious burger',
            price=1000,
            restaurant=self.restaurant
        )
        self.order_data = {
            'customer': self.customer,
            'menu': self.menu,
            'status': 'pending'
        }

    def test_create_order(self):
        order = Order.objects.create(**self.order_data)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.menu, self.menu)
        self.assertEqual(order.menu.restaurant, self.menu.restaurant)
        self.assertEqual(order.menu.restaurant, self.restaurant)

        self.assertEqual(order.status, 'pending')

    def test_order_str_method(self):
        order = Order.objects.create(**self.order_data)
        self.assertEqual(str(order), f"Order {order.id}")
