from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework import generics


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DeleteTask(generics.DestroyAPIView):
    queryset = Task.objects.all()
    lookup_field = 'id'
    serializer_class = TaskSerializer

class UpdateTask(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    lookup_field = 'id'
    serializer_class = TaskSerializer