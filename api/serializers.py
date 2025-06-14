from rest_framework import serializers

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    bio = serializers.CharField()