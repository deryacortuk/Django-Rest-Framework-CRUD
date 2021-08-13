from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import FollowerModel
from .serializers import FollowerSerializer
from rest_framework import permissions

# Create your views here.

class FollowerListView(ListCreateAPIView):
    
    serializer_class = FollowerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(follower =self.request.user)
        
    def get_queryset(self):
        return FollowerModel.objects.filter(follower=self.request.user)
    

class FollowerDetailView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = FollowerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    lookup_field ='id'
        
    def get_queryset(self):
        return FollowerModel.objects.filter(follower=self.request.user)

