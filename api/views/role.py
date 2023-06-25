from rest_framework.generics import (
    ListCreateAPIView as LC, RetrieveUpdateDestroyAPIView as RUD,
    RetrieveAPIView as R, DestroyAPIView as D,
    )

from api.models.role import Role
from api.models import User

from api.serializers import RoleSerializer


class RoleListAPIView(LC):
    """
    GET role/ List all roles
    POST role/ Create a new role
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetailAPIView(RUD):
    """
    GET role/:id/ Retrieve a role
    PUT role/:id/ Update a role
    DELETE role/:id/ Delete a role
    PATCH role/:id/ Partially update a role
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# User Roles

class UserRolesListAPIView(LC):
    serializer_class = RoleSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Role.objects.filter(user_id=user_id)
    
    def perform_create(self, serializer):
        user_id = self.kwargs['user_id']
        user = User.objects.get(id=user_id)
        serializer.save(user=user)


class UserRolesDetailAPIView(R,D):
    serializer_class = RoleSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Role.objects.filter(user_id=user_id)

    def get_object(self):
        user_id = self.kwargs['user_id']
        role_id = self.kwargs['role_id']
        return Role.objects.get(user_id=user_id, id=role_id)

