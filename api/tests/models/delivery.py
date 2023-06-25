from django.test import TestCase
from api.models import Order, User, Delivery, Restaurant, Menu

class DeliveryModelTestCase(TestCase):
    def setUp(self):

        self.delivery_status_choices = [
        ('pending', 'Pending'),
        ('en_route', 'En route'),
        ('completed', 'Completed'),
    ]
        self.customer = User.objects.create(
            first_name='Test',
            last_name='User',
            email='test@example.com',
            password='testpassword'
        )
        self.restaurant = Restaurant.objects.create(
            name='ABC Restaurant',
            description='A great place to dine.',
            owner_id=self.customer.id
        )
        self.menu = Menu.objects.create(
            name='Burger',
            description='Delicious burger',
            price=1000,
            restaurant=self.restaurant
        )
        self.order = Order.objects.create(
            customer=self.customer,
            menu=self.menu,
            status='pending'
        )
        self.delivery_agent = User.objects.create(
            first_name='Delivery',
            last_name='Agent',
            email='delivery@example.com',
            password='deliverypassword'
        )
        self.delivery_data = {
            'order': self.order,
            'delivery_agent': self.delivery_agent,
            'status': 'pending'
        }

    def test_create_delivery(self):
        delivery = Delivery.objects.create(**self.delivery_data)
        self.assertEqual(Delivery.objects.count(), 1)
        self.assertEqual(delivery.order, self.order)
        self.assertEqual(delivery.delivery_agent, self.delivery_agent)
        self.assertEqual(delivery.status, 'pending')

    def test_delivery_str_method(self):
        delivery = Delivery.objects.create(**self.delivery_data)
        self.assertEqual(str(delivery), f"Delivery {delivery.id}")

    def test_status_choices(self):
        delivery = Delivery.objects.create(**self.delivery_data)
        status_choices = [choice[0] for choice in self.delivery_status_choices]
        self.assertIn(delivery.status, status_choices)
