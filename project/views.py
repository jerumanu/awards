from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Profile, Projects
from .serializer import  ProfileSerializer,ProjectsSerializer
# Create your views here.
