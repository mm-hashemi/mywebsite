from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import ProfileViewSet, SkillViewSet, ProjectViewSet

router = DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('skills', SkillViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]