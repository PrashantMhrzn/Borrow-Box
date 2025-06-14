from django.urls import path, include
from .views import *

urlpatterns = [
    path('author', author_list)
]