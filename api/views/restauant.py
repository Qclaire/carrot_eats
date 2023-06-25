from rest_framework.generics import ListAPIView
from rest_framework.generics import ListCreateAPIView as LC
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView as RUD
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from api.models import Restaurant
from api.serializers import RestaurantSerializer


class RestaurantListAPIView(LC):
    """
    GET restaurant/ List all restaurants
    POST restaurant/ Create a new restaurant
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetailAPIView(RUD):
    """
    GET restaurant/:id/ Retrieve a restaurant
    PUT restaurant/:id/ Update a restaurant
    DELETE restaurant/:id/ Delete a restaurant
    PATCH restaurant/:id/ Partially update a restaurant
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer



class UserRestaurantsAPIView(ListAPIView):
    """
    GET user/:user_id/restaurants/ List all restaurants owned by a user
    """
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Restaurant.objects.filter(owner_id=user_id)


class AssignRestaurantAPIView(UpdateAPIView):
    """
    PUT user/:user_id/restaurants/:restaurant_id/ Assign a restaurant to a user
    """
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return Restaurant.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
