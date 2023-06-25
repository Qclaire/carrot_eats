from rest_framework.generics import (
    ListCreateAPIView as LC, RetrieveUpdateDestroyAPIView as RUD, ListAPIView,
)


from api.models import Order
from api.permissions import CanCreateOrderPermission

from api.serializers import OrderSerializer


class OrderListAPIView(LC):
    """
    GET order/ List all orders
    POST order/ Create a new order
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CanCreateOrderPermission]


class OrderDetailAPIView(RUD):
    """
    GET order/:id/ Retrieve an order
    PUT order/:id/ Update an order
    DELETE order/:id/ Delete an order
    PATCH order/:id/ Partially update an order
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserOrdersAPIView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Order.objects.filter(customer_id=user_id)