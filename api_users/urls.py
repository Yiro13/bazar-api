from rest_framework import routers
from .api import UserViewSet, verificar_existencia_usuario
from django.urls import path
#from rest_framework.decorators import api_view

router = routers.DefaultRouter()
router.register('api/usuarios', UserViewSet, 'usuarios')

urlpatterns = [
    *router.urls,
    path('api/usuarios/verificar-existencia', verificar_existencia_usuario, name='verificar-existencia'),
]