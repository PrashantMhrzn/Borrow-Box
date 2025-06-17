from django.urls import path, include
from .views import *

urlpatterns = [
    path('author', AuthorList.as_view()),
    path('author/<id>', AuthorDetail.as_view()),
    path('genre', GenreList.as_view()),
    path('genre/<id>', GenreDetail.as_view()),
    path('book', BookList.as_view()),
]