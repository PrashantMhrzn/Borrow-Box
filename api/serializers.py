from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'category', 'description']

class BookSerializer(serializers.ModelSerializer):
    # If you only use PrimaryKeyRelatedField, you only get IDs for GET.
    # If you only use SlugRelatedField, you can’t POST or PUT using IDs.
   
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source='author', write_only=True
    )
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), source='genre', write_only=True
    )
    
    author = serializers.StringRelatedField(read_only=True)
    genre = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_id', 'published_date', 'genre', 'genre_id', 'available_copies']
    
