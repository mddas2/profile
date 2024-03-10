from rest_framework import serializers
from ..models import Blogs

class BlogsReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'

class BlogsWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'