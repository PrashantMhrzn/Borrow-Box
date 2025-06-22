from django.urls import path
from .views import *

urlpatterns = [
    path('user', LoginAPIView.as_view())
]
