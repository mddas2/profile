from rest_framework import serializers
from ..models import Projects

class ProjectsReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class ProjectsWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'