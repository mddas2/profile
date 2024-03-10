from ..models import Experience
from ..serializers.experience_serializers import ExperienceReadSerializers,ExperienceWriteSerializers
from ..utilities.importbase import *

class ExperienceViewSets(viewsets.ModelViewSet):
    serializer_class = ExperienceReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Experience.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return ExperienceWriteSerializers
        return super().get_serializer_class()
    