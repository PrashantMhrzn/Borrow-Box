from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    bio = serializers.CharField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)