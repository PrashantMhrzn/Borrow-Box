from django.urls import path, include
from .views import *

urlpatterns = [
    path('author', AuthorList.as_view()),
    path('author/<id>', AuthorDetail.as_view()),
    path('genre', GenreList.as_view()),
    path('genre/<id>', GenreDetail.as_view()),
    path('book', BookList.as_view()),
    path('book/<id>', BookDetail.as_view()),
    path('review', ReviewList.as_view()),
    path('review/<id>', ReviewDetail.as_view()),
    path('reserve', ReserveList.as_view()),
    path('reserve/<id>', ReserveDetail.as_view()),
    path('borrow', BorrowList.as_view()),
    path('borrow/<id>', BorrowDetail.as_view()),
]