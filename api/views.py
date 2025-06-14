from django.shortcuts import render
from rest_framework.decorators import api_view
# we use this response for api view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == 'GET':
        # Load data from the db
        authors = Author.objects.all()
        # Serializer
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        authors = Author.objects.all()
        serializer = AuthorSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "Detail": "New Category Added!"
        })

@api_view(['GET', 'POST', 'DELETE'])
def author_detail(request, id):
    if request.method == 'GET':
        authors = Author.objects.get(id = id)
        serializer = AuthorSerializer(authors)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        authors = Author.objects.get(id = id)
        authors.delete()
        return Response({
            "Detail": "Author deleted!"
        })