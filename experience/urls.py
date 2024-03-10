from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import experience_viewsets, profession_category_viewsets,skills_viewsets

router = DefaultRouter()

router.register('job-category', profession_category_viewsets.ProfessionCategoryViewSets, basename="ProfessionCategoryViewSets")
router.register('jobs', experience_viewsets.ExperienceViewSets, basename="jobs")
router.register('skills', skills_viewsets.SkillsViewSets, basename="SkillsViewSets")

urlpatterns = [    
    path('', include(router.urls)),
]