from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models import User
from api.permissions import IsAdminOrManagerOrSelf
from api.serializers import UserSerializer

from djoser.views import UserViewSet as DjoserUserViewSet


class UserViewSet(DjoserUserViewSet):
    lookup_field = 'pk'
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrManagerOrSelf]

class UserListAPIView(APIView):
    """
    List all users, or create a new user.
    """
    permission_classes = [IsAuthenticated]  # Add permission class for listing users

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    permission_classes = [AllowAny]  # Add permission class for creating a user

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    permission_classes = [IsAuthenticated]  # Add permission class for retrieving, updating, and deleting a user

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
