from django.shortcuts import render
from rest_framework.decorators import api_view
# we use this response for api view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema

class AuthorList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
        authors = Author.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(authors, request)
        serializer = AuthorSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @extend_schema(request=AuthorSerializer, responses=AuthorSerializer)
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Detail": "New Author Added!"})

class AuthorDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        authors = Author.objects.get(id = id)
        serializer = AuthorSerializer(authors)
        return Response(serializer.data)
    
    def delete(self, request, id):
        author = Author.objects.get(id=id)
        if Book.objects.filter(author=author).exists():
            return Response({"Detail": "This author cannot be deleted. Book with this author exists."})
        author.delete()
        return Response({"Detail": "Author deleted successfully."})
    
    @extend_schema(request=AuthorSerializer, responses=AuthorSerializer)
    def put(self, request, id):
        author = Author.objects.get(id = id)
        serializer = AuthorSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "Detail": "Author updated!"
        })
    
    @extend_schema(request=AuthorSerializer, responses=AuthorSerializer)
    def patch(self, request, id):
        author = Author.objects.get(id = id)
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "Detail": "Author updated Partially!"
        })


class GenreList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        genre = Genre.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(genre, request)
        serializer = GenreSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    @extend_schema(request=GenreSerializer, responses=GenreSerializer)        
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"Detail": "New Genre Added!"})
    
class GenreDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    
    @extend_schema(request=GenreSerializer, responses=GenreSerializer)   
    def put(self, request, id):
        genre = Genre.objects.get(id = id)
        serializer = GenreSerializer(genre, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({ 
            "Detail": "Genre Updated!"
        })
    
    @extend_schema(request=GenreSerializer, responses=GenreSerializer)   
    def patch(self, request, id):
        genre = Genre.objects.get(id = id)
        serializers = GenreSerializer(genre, data=request.data, partial=True)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response({
            "Detail": "Genre updated Partially!"
        })
    
class BookList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        books = Book.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(books, request)
        serializer = BookSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    @extend_schema(request=BookSerializer, responses=BookSerializer)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class BookDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        book = Book.objects.get(id = id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def delete(self, request, id):
        book = Book.objects.get(id=id)
        if Review.objects.filter(book=book).exists() or Reserve.objects.filter(book=book).exists() or Borrow.objects.filter(book=book).exists():
            return Response({"Detail": "This book cannot be deleted. Related reviews/reservations/borrows exist."})
        book.delete()
        return Response({"Detail": "Book deleted successfully."})
    
    @extend_schema(request=BookSerializer, responses=BookSerializer)
    def put(self, request, id):
        book = Book.objects.get(id = id)
        serializer = BookSerializer(book, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "Detail": "Book Succesfully Updated!"
        })
    
    @extend_schema(request=BookSerializer, responses=BookSerializer)
    def patch(self, request, id):
        book = Book.objects.get(id = id)
        serializer = BookSerializer(book, data = request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "Detail": "Book Partially Updated!"
        })
    
class ReviewList(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(reviews, request)
        serializer = ReviewSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @extend_schema(request=ReviewSerializer, responses=ReviewSerializer)   
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class ReviewDetail(APIView):
    def get(self, request, id):
        review = Review.objects.get(id = id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    def delete(self, request, id):
        review = Review.objects.get(id = id)
        review.delete()
        return Response({
            "Detail": "Review Succesfully Deleted!"
        })
    
    @extend_schema(request=ReviewSerializer, responses=ReviewSerializer)  
    def put(self, request, id):
        review = Review.objects.get(id = id)
        serializer = ReviewSerializer(review, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "Detail": "Review Succesfully Updated!"
        })
    
    @extend_schema(request=ReviewSerializer, responses=ReviewSerializer)  
    def patch(self, request, id):
        review = Review.objects.get(id = id)
        serializer = ReviewSerializer(review, data = request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "Detail": "Review Partially Updated!"
        })

class ReserveList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        reserves = Reserve.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(reserves, request)
        serializer = ReserveSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @extend_schema(request=ReserveSerializer, responses=ReserveSerializer)  
    def post(self, request):
        serializer = ReserveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class ReserveDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        reserve = Reserve.objects.get(id = id)
        serializer = ReserveSerializer(reserve)
        return Response(serializer.data)
    
    def delete(self, request, id):
        reserve = Reserve.objects.get(id = id)
        reserve.delete()
        return Response({
            "Detail": "Reserve Succesfully Deleted!"
        })
    
    @extend_schema(request=ReserveSerializer, responses=ReserveSerializer)  
    def put(self, request, id):
        reserve = Reserve.objects.get(id = id)
        serializer = ReserveSerializer(reserve, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "Detail": "Reserve Succesfully Updated!"
        })
    
    @extend_schema(request=ReserveSerializer, responses=ReserveSerializer)  
    def patch(self, request, id):
        reserve = Reserve.objects.get(id = id)
        serializer = ReserveSerializer(reserve, data = request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "Detail": "Reserve Succesfully Updated!"
        })
    
   
class BorrowList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        borrows = Borrow.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(borrows, request)
        serializer = BorrowSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @extend_schema(request=BorrowSerializer, responses=BorrowSerializer)  
    def post(self, request):
        serializer = BorrowSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class BorrowDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        reserve = Borrow.objects.get(id = id)
        serializer = BorrowSerializer(reserve)
        return Response(serializer.data)
    
    def delete(self, request, id):
        reserve = Borrow.objects.get(id = id)
        reserve.delete()
        return Response({
            "Detail": "Borrowed book Succesfully Deleted!"
        })
    

    
   