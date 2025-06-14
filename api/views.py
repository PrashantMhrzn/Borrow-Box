from django.shortcuts import render
from rest_framework.decorators import api_view
# we use this response for api view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])
def author_list(request):
	# Load data from the db
	authors = Author.objects.all()
	# Serializer
	serializer = AuthorSerializer(authors, many=True)
	return Response(serializer.data)