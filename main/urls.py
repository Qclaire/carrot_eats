# from django.urls import include, path
# # from djoser import views as djoser_views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )
# from api.views.restauant import RestaurantDetailAPIView, RestaurantListAPIView


# from api.views.user import UserViewSet
# urlpatterns = [
#     path('api/users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
#     path('api/users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
    
#     # Simple JWT URLs
#     path('api/token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

#     # Restaurants
#     path('api/restaurants/', RestaurantListAPIView.as_view(), name='restaurant-list'),
#     path('api/restaurants/<int:pk>/', RestaurantDetailAPIView.as_view(), name='restaurant-detail'),
# ]


from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework import routers
from api.views.delivery import DeliveryDetailAPIView, DeliveryListAPIView
from api.views.menu import MenuDetailAPIView, MenuListAPIView
from api.views.order import OrderDetailAPIView, OrderListAPIView, UserOrdersAPIView
from api.views.role import RoleDetailAPIView, RoleListAPIView, UserRolesDetailAPIView, UserRolesListAPIView
from api.views.user import UserViewSet
from api.views.restauant import AssignRestaurantAPIView, RestaurantDetailAPIView, RestaurantListAPIView, UserRestaurantsAPIView

# Import necessary Swagger-related modules
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Create a router for the UserViewSet
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Define schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Carrot Eats API",
        default_version='v1',
        description="API For the Carrot eats app",
        license=openapi.License(name="BSD License"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # DRF URLs
    path('api/', include(router.urls)),

    path('api/users/<int:user_id>/orders/', UserOrdersAPIView.as_view(), name='user-orders'),

    # Simple JWT URLs
    path('api/token/login/', TokenObtainPairView.as_view(), name='Obtain JWT token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='Refresh JWT token'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='Verify JWT token'),

    # Restaurants
    path('api/restaurants/', RestaurantListAPIView.as_view(), name='restaurant'),
    path('api/restaurants/<int:pk>/', RestaurantDetailAPIView.as_view(), name='restaurant-detail'),

    # Restaurant Menu
    path('api/restaurants/<int:pk>/menu/', MenuListAPIView.as_view(), name='menu'),
    path('api/restaurants/<int:pk>/menu/<int:id>/', MenuDetailAPIView.as_view(), name='menu-detail'),
    path('api/users/<int:user_id>/restaurants/', UserRestaurantsAPIView.as_view(), name='user-restaurants'),
    path('api/restaurants/<int:pk>/assign/', AssignRestaurantAPIView.as_view(), name='assign-restaurant'),
    
    # Menu
    path('api/menu/', MenuListAPIView.as_view(), name='menu'),
    path('api/menu/<int:id>/', MenuDetailAPIView.as_view(), name='menu-detail'),

    # Orders
    path("api/orders/", OrderListAPIView.as_view(), name="order-list"),
    path("api/orders/<int:pk>/", OrderDetailAPIView.as_view(), name="order-detail"),

    # Delivery
    path("api/delivery/", DeliveryListAPIView.as_view(), name="delivery-list"),
    path("api/delivery/<int:pk>/", DeliveryDetailAPIView.as_view(), name="delivery-detail"),

    # # Roles
    # path("api/roles/", RoleListAPIView.as_view(), name="role-list"),
    # path("api/roles/<int:pk>/", RoleDetailAPIView.as_view(), name="role-detail"),
    

    # Swagger Documentation
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]