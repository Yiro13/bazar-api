from rest_framework import routers
from django.urls import path
from .api import ProductoViewSet, CategoriaViewSet, verificar_existencia_producto_por_categoria

router = routers.DefaultRouter()
router.register('api/productos', ProductoViewSet, 'productos')
router.register('api/categorias', CategoriaViewSet, 'categorias')

urlpatterns = [
    *router.urls,
    path('api/productos/consultar-categoria', verificar_existencia_producto_por_categoria, name='verificar-categoria'),
]