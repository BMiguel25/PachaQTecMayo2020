from rest_framework import viewsets
from rest_framework import permissions
from pedidos.serializers import TipoClienteSerializer, TipoProductoSerializer
from pedidos.models import tipoCliente, tipoProducto
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class TipoClienteViewSet(viewsets.ModelViewSet):
    serializer_class = TipoClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        queryset = tipoCliente.objects.all()
        desc = self.request.query_params.get('desc',None)
        if desc is not None:
            queryset = queryset.filter(descripcion=desc)
        return queryset

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = tipoProducto.objects.all()
    serializer_class = TipoProductoSerializer
    permission_classes = [permissions.IsAuthenticated]
    #filter_backends = [DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    #search_fields = ['username', 'email']
    search_fields=['descripcion','isActivo']