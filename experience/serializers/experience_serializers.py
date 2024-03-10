from rest_framework import serializers
from ..models import Experience

class ExperienceReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class ExperienceWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'