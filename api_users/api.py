from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

@api_view(['GET'])
def verificar_existencia_usuario(request):
    nombre_usuario = request.query_params.get('nombre')
    try:
        user = User.objects.get(nombre = nombre_usuario)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'mensaje': 'El usuario no existe'}, status=404)