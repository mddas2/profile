from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import blogs_viewsets

router = DefaultRouter()

router.register('blogs', blogs_viewsets.BlogsViewSets, basename="BlogsViewSets")


urlpatterns = [    
    path('', include(router.urls)),
]