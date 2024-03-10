from ..models import Projects
from ..serializers.projects_serializers import ProjectsReadSerializers,ProjectsWriteSerializers
from ..utilities.importbase import *

class ProjectsViewSets(viewsets.ModelViewSet):
    serializer_class = ProjectsReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Projects.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return ProjectsWriteSerializers
        return super().get_serializer_class()
    