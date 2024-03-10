from ..models import Blogs
from ..serializers.blogs_serializers import BlogsReadSerializers,BlogsWriteSerializers
from ..utilities.importbase import *

class BlogsViewSets(viewsets.ModelViewSet):
    serializer_class = BlogsReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Blogs.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return BlogsWriteSerializers
        return super().get_serializer_class()
    