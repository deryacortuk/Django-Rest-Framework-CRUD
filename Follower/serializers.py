from django.db import models
from rest_framework import serializers
from .models import FollowerModel

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = FollowerModel
        
        fields = ['fullname','picture','is_favorite']


