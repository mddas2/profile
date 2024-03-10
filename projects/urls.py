from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import projects_viewsets

router = DefaultRouter()

router.register('projects', projects_viewsets.ProjectsViewSets, basename="ProjectsViewSets")


urlpatterns = [    
    path('', include(router.urls)),
]