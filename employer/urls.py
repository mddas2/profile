from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import employer_viewsets

router = DefaultRouter()

router.register('employer', employer_viewsets.EmployerViewSets, basename="EmployerViewSets")


urlpatterns = [    
    path('', include(router.urls)),
]