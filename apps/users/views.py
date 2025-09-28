from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import User
from .serializers import UserCreateSerializer, UserListSerializer


class UserCreateView(generics.CreateAPIView):
    """ Vista para crear usuarios """
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Guardar el usuario 
            return Response(
                {"message": "Usuario creado correctamente"}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(generics.RetrieveAPIView):
    """ Vista para obtener un usuario por su ID """
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserListView(generics.ListAPIView):
    """ Vista para listar usuarios """
    queryset = User.objects.all()
    serializer_class = UserListSerializer
