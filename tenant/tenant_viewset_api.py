from rest_framework import viewsets
from django.db import connection
from .models import Domain,DomainTenantAwareModel
from .tenant_serializers import DomainSerializer,DomainTenantAwareModelSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

class DomainViewSet(viewsets.ModelViewSet):
    queryset = DomainTenantAwareModel.objects.all()
    serializer_class = DomainTenantAwareModelSerializer