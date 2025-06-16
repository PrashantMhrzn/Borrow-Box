from django.shortcuts import render
from rest_framework.decorators import api_view
# we use this response for api view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

class AuthorList(APIView):
    def get(self, request):
        # Load data from the db
        authors = Author.objects.all()
        # Serializer
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "Detail": "New Author Added!"
        })

class AuthorDetail(APIView):
    def get(self, request, id):
        authors = Author.objects.get(id = id)
        serializer = AuthorSerializer(authors)
        return Response(serializer.data)
    
    def delete(self, request, id):
        author = Author.objects.get(id = id)
        author.delete()
        return Response({
            "Detail": "Author deleted!"
        })
    
    def put(self, request, id):
        author = Author.objects.get(id = id)
        serializers = AuthorSerializer(author, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({
            "Detail": "Author updated!"
        })


class GenreList(APIView):
    def get(self, request):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializers = GenreSerializer(data = request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({ 
            "Detail": "New Genre Added!"
        })
    
class GenreDetail(APIView):
    def get(self, request, id):
        genre = Genre.objects.get(id = id)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)
    
    def delete(self, request, id):
        genre = Genre.objects.get(id = id)
        check = Book.objects.filter(genre = genre)
        if check:
            return Response({ 
            "Detail": "This genre cannot be deleted. Book with this genre exists"
        })
        genre.delete()
        return Response({ 
            "Detail": "Genre Deleted!"
        })
    