from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .serializers import studentSerializer
from .models import student

class Student(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
