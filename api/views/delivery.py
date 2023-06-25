from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView as LC, RetrieveUpdateDestroyAPIView as RUD

from api.models import Order
from api.serializers import OrderSerializer



class DeliveryListAPIView(LC):
    """
    GET delivery/ List all deliveries
    POST delivery/ Create a new delivery
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = []


class DeliveryDetailAPIView(RUD):
    """
    GET delivery/:id/ Retrieve a delivery
    PUT delivery/:id/ Update a delivery
    DELETE delivery/:id/ Delete a delivery
    PATCH delivery/:id/ Partially update a delivery
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = []

    