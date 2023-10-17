from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('api/books/', BooksViewSet.as_view({'post': 'create', 'get': 'list'})),
    path('api/books/<int:pk>', BooksViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/author/', AuthorViewSet.as_view({'post': 'create', 'get': 'list'})),
    path('api/author/<uuid:pk>', AuthorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]