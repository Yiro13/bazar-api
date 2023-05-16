from .models import Producto, Categoria
from rest_framework import viewsets, permissions
from .serializers import ProductoSerializer, CategoriaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaSerializer

@api_view(['GET'])
def verificar_existencia_producto_por_categoria(request):
    categoria_id = request.query_params.get('categoria_id')
    try:
        productos = Producto.objects.filter(categoria=categoria_id)
        if productos.exists():
            serializer = ProductoSerializer(productos, many=True)
            return Response(serializer.data)
        else:
            return Response({'mensaje': 'No hay productos en esta categoría.'})
    except Categoria.DoesNotExist:
        return Response({'mensaje': 'La categoría no existe'}, status=404)
