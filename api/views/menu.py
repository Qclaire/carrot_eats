from rest_framework.generics import ListCreateAPIView as LC
from rest_framework.generics import RetrieveUpdateDestroyAPIView as RUD

from api.models import Menu
from api.serializers import MenuSerializer


from rest_framework.permissions import IsAuthenticated, AllowAny


class MenuListAPIView(LC):
    """
    GET menu/ List all menus
    POST menu/ Create a new menu
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated,AllowAny]


class MenuDetailAPIView(RUD):
    """
    GET menu/:id/ Retrieve a menu
    PUT menu/:id/ Update a menu
    DELETE menu/:id/ Delete a menu
    PATCH menu/:id/ Partially update a menu
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated,AllowAny]
