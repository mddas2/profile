from ..models import Company
from ..serializers.profession_category_serializers import ProfessionCategoryReadSerializers,ProfessionCategoryWriteSerializers
from ..utilities.importbase import *

class ProfessionCategoryViewSets(viewsets.ModelViewSet):
    serializer_class = ProfessionCategoryReadSerializers
    permission_classes = [AdminViewSetsPermission]
    authentication_classes = [JWTAuthentication]
    pagination_class = MyPageNumberPagination
    queryset  = Company.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return ProfessionCategoryWriteSerializers
        return super().get_serializer_class()
    