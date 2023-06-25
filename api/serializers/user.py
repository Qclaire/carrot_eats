from djoser.serializers import UserCreateSerializer, UserSerializer
from api.models import User

class UserRegistrationSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'role',"last_login", "is_active", "created_at", "last_modified")

class UserSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        model = User
        fields = ("id", "email", "first_name", "last_name", "role", "last_login", "is_active", "created_at", "last_modified")
        ref_name = "CustomUserSerializer"
