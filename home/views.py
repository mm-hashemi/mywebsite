from rest_framework import viewsets
from .models import Profile, Skill, Project
from .serializers import ProfileSerializer, SkillSerializer, ProjectSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

@method_decorator(csrf_exempt, name='dispatch')
class ProfileViewSet(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

@method_decorator(csrf_exempt, name='dispatch')
class SkillViewSet(APIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

@method_decorator(csrf_exempt, name='dispatch')
class ProjectViewSet(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    