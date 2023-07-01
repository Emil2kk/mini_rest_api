from rest_framework import serializers
from .models import Cars
class Carspec(serializers.ModelSerializer):
    class Meta:
        model=Cars
        fields=['id','base','motor']
        
    