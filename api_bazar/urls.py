from rest_framework import routers
from .api import ProductoViewSet, CategoriaViewSet

router = routers.DefaultRouter()
router.register('api/productos', ProductoViewSet, 'productos')
router.register('api/categorias', CategoriaViewSet, 'categorias')

urlpatterns = router.urls