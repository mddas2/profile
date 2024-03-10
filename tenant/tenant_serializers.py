from rest_framework import serializers
from .models import Domain, DomainTenantAwareModel

class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = '__all__'
    
class  DomainTenantAwareModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainTenantAwareModel
        fields = '__all__'