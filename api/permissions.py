from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny

RESTAURANT_MANAGER_ROLE = "RESTAURANT_MANAGER"
DELIVERY_AGENT_ROLE = "DELIVERY_AGENT"
ADMIN_ROLE = "ADMIN"
CUSTOMER_ROLE = "CUSTOMER"

Roles = [RESTAURANT_MANAGER_ROLE, DELIVERY_AGENT_ROLE, ADMIN_ROLE, CUSTOMER_ROLE]


class IsAdminOrManagerOrSelf(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.role == ADMIN_ROLE and request.user.is_authenticated
        if view.action == 'destroy' or view.action == 'update' or view.action == 'partial_update':
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
            if view.action == 'destroy' or view.action == 'update' or view.action == 'partial_update':
              return obj.id == request.user.id or request.user.role == ADMIN_ROLE
            return True
    



class IsOrderOwnerOrManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == CUSTOMER_ROLE or request.user.role == RESTAURANT_MANAGER_ROLE

    def has_object_permission(self, request, view, obj):
        return obj.customer_id == request.user.id or request.user.role == RESTAURANT_MANAGER_ROLE


class CanCreateOrderPermission(BasePermission):
    """
    Allows only authenticated customers and restaurant managers to create or list orders
    """
    def has_permission(self, request, view):
        return (
            IsAuthenticated and
            (
            request.user.role == RESTAURANT_MANAGER_ROLE or
            request.user.role == CUSTOMER_ROLE
            )
        )
    
