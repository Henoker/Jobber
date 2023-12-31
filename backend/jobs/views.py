from django.shortcuts import render
from rest_framework import generics 

from .models import Job
from .serializers import JobSerializer

# Create your views here.
class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    