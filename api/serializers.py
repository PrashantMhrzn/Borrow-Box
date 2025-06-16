from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    bio = serializers.CharField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        return instance
    
class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.CharField()
    description = serializers.CharField()

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.description)
        