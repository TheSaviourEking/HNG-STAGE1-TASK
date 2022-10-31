from rest_framework import serializers
from .models import GetApi

class GetApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetApi
        fields = '__all__'