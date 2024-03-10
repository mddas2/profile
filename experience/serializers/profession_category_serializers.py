from rest_framework import serializers
from ..models import ProfessionCategory

class ProfessionCategoryReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfessionCategory
        fields = '__all__'

class ProfessionCategoryWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfessionCategory
        fields = '__all__'