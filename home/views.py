from rest_framework import viewsets
from .models import Profile, Skill, Project
from .serializers import ProfileSerializer, SkillSerializer, ProjectSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response

@method_decorator(csrf_exempt, name='dispatch')
class ProfileViewSet(APIView):
    def get(self, request):
        profiles= Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return  Response(serializer.data)
    

@method_decorator(csrf_exempt, name='dispatch')
class SkillViewSet(APIView):
    def get(self, request):
        skills = Skill.objects.all()         
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

@method_decorator(csrf_exempt, name='dispatch')

class ProjectViewSet(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)